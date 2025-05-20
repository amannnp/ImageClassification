from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
import numpy as np
import json
from PIL import Image

# model will load from h5, not mainscript
# so to change model first re-run mainscript and save model
# model will fetch here through fastapi

model = load_model("cifar100_model.h5", compile=False)

with open("cifar_labels.json", "r") as f:
    class_names = json.load(f)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#preprocessing uploaded image 
#to align with our original dataset

def preprocess(img: Image.Image):
    img = img.resize((32, 32))
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img = Image.open(file.file).convert("RGB")
    processed_img = preprocess(img)
    preds = model.predict(processed_img)[0]
    pred_class = int(np.argmax(preds))
    confidence = float(np.max(preds))

    return {
        "predicted_class": class_names[pred_class],
        "confidence": confidence
    }
