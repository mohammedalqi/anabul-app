import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

from flask import Flask, jsonify, request
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

model_path = "Klasifikasi 5 Ras Anjing.h5"  # Path to your trained model
class_labels = [
    "French Bulldog",
    "German Shepherd",
    "Golden Retriever",
    "Poodle",
    "Yorkshire Terrier",
]

# Load the model
model = load_model(model_path)


@app.route("/", methods=["GET"])
def index():
    return "The server is running!"


# Define the route for predictions
@app.route("/breed/dog", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Retrieve the uploaded image
        file = request.files["file"]
        img = Image.open(file)
        img = img.resize((224, 224))
        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        # Make predictions
        predictions = model.predict(img)
        class_index = np.argmax(predictions)
        predicted_class = class_labels[class_index]
        confidence = predictions[0][class_index] * 100

        # Return the prediction result as JSON
        result = {"Breed Prediction": [predicted_class]}
        return jsonify(result)

    return "Use the POST method to access this route."


if __name__ == "__main__":
    app.run(debug=True)
