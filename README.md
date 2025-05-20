This project involves building an image classification system using the CIFAR-100 dataset. It includes developing a deep learning model to accurately categorize images into 100 different classes. The workflow covers data preprocessing, model training, evaluation, and optimization for improved accuracy. The project also includes deploying the trained model with a FastAPI backend and an HTML-based frontend, allowing users to upload images and receive classification results in real time.

Tech Stack - Python, TensorFlow (Keras), FastAPI, HTML, CSS, JavaScript

****************************Important Note****************************

To clone this project, type on git bash : git clone "https://github.com/amannnp/ImageClassification.git"
You need to manually load the API for prediction.


----------------------------------------------------------------------
Project Pipeline --

1) mainscript.py - The main data loading, training and evaluation script. It saves the file "cifar100_model.h5"
2) cifar100_model.h5 - DO NOT manipulate this model. In order for future improvements, make changes in the 'mainscript.py'. From there, this file will be automatically updated.
3) mainapi.py - It's the main backend API script. It starts the API, loads the model and defines the API endpoints that the frontend/client calls. It also handles incoming requests and data preprocessing. Then it also returns the predictions back to the client.
4) generate_labels - is used to create the 'cifar_labels.json' file through script incase any error comes.


NOTE - TO START YOUR API, GO TO COMMAND AND IN THE SAME FILE DIRECTORY, TYPE - "uvicorn mainapi:app --reload" 
THIS WILL RUN THE API SCRIPT, HERE 'mainapi' is your filename of main API Backend. 
   +-----------------+
| Data Collection |
+--------+--------+
         |
         v
+---------------------+
| Data Preprocessing   |
+---------+-----------+
          |
          v
+---------------------+
|   Model Design      |
+---------+-----------+
          |
          v
+---------------------+
|   Model Training    |
+---------+-----------+
          |
          v
+---------------------+
|  Model Evaluation   |
+---------+-----------+
          |
          v
+---------------------+
|  Model Optimization |
+---------+-----------+
          |
          v
+---------------------+
|  Model Conversion   |
+---------+-----------+
          |
          v
+---------------------+
| Backend Development |
+---------+-----------+
          |
          v
+---------------------+
| Frontend Development|
+---------+-----------+
          |
          v
+---------------------+
| Integration & Testing|
+---------+-----------+
          |
          v
+---------------------+
|     Deployment      |
+---------------------+
--------------------------------------------------------------------------------
