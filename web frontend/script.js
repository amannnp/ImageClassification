function uploadImage() {
  const fileInput = document.getElementById("imageInput");
  const preview = document.getElementById("preview");
  const result = document.getElementById("result");
  const loader = document.getElementById("loader");

  const file = fileInput.files[0];
  if (!file) {
    alert("Please select an image file.");
    return;
  }

  // image preview
  const reader = new FileReader();
  reader.onload = function (e) {
    preview.innerHTML = `<img src="${e.target.result}" alt="Image Preview">`;
  };
  reader.readAsDataURL(file);

  // prepare request
  const formData = new FormData();
  formData.append("file", file);

  loader.classList.remove("hidden");
  result.textContent = "";

  // req goes to API backend through here 
  fetch("http://127.0.0.1:8000/predict", {
    method: "POST",
    body: formData
  })
    .then(response => response.json())
    .then(data => {
      loader.classList.add("hidden");
      result.textContent = `Predicted Class: ${data.predicted_class}`;
    })
    .catch(error => {
      loader.classList.add("hidden");
      result.textContent = "Error occurred during prediction.";
      console.error(error);
    });
}
