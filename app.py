from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
MODEL_PATH = r'C:\Users\chari\fight_detect\data\fight_detection_model.h5'
model = load_model(MODEL_PATH)

# Directory to save uploaded images
UPLOAD_FOLDER = 'static/uploaded_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file part"
    file = request.files['image']
    if file.filename == '':
        return "No selected file"

    # Save the uploaded image
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    try:
        # Preprocess the image using Pillow
        img = Image.open(file_path).convert('RGB')  # Ensure image is RGB
        img = img.resize((224, 224))  # Resize the image
        img_array = np.array(img) / 255.0  # Normalize pixel values to [0, 1]
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

        # Predict the class
        prediction = model.predict(img_array)
        label = "Violent" if prediction[0][0] > 0.5 else "Non-Violent"
        confidence = prediction[0][0] if prediction[0][0] > 0.5 else 1 - prediction[0][0]

        # Render the result
        return render_template('index.html', prediction=label, confidence=f"{confidence * 100:.2f}%", image_path=file_path)
    except Exception as e:
        return f"Error processing image: {e}"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
