# Fight Detection Web Application

## Overview
The **Fight Detection Web App** is a machine learning-powered tool designed to classify images as "Violent" or "Non-Violent." This application combines a pre-trained CNN (Convolutional Neural Network) model with a user-friendly web interface built using Flask.

---

## Features
- **Image Classification**: Users can upload an image to determine if it depicts violence.
- **Confidence Score**: Displays the model's confidence in its prediction.
- **Web Interface**: Intuitive and visually appealing UI for user interaction.
- **Scalable**: Easy to extend to classify videos or enable real-time detection.

---

## Folder Structure
```
fight_detection_web_app/
├── app.py                  # Flask application (main script)
├── fight_detection_model.h5 # Trained CNN model
├── templates/              # HTML templates
│   └── index.html          # Web page UI
├── static/                 # Static files
│   ├── styles.css          # CSS for styling the UI
│   └── uploaded_images/    # Directory for uploaded images
└── README.md               # Project documentation (this file)
```

---

## Prerequisites
Ensure the following are installed:
- **Python 3.8+**
- **Pip**
- Virtual Environment (optional but recommended)

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Barla-Charishma/fight-detection-web-app.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fight_detection_web_app
   ```
3. Set up a virtual environment (optional):
   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/Mac
   env\Scripts\activate    # For Windows
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```
3. Upload an image and view the prediction result.

---

## Model Details
- **Framework**: TensorFlow/Keras
- **Architecture**: CNN
- **Dataset**: Trained on a dataset of violent and non-violent images.

---

## Known Issues
1. **Large Images**: Uploading very large images may slow down predictions.
2. **Accuracy**: Model performance can be improved by fine-tuning or using transfer learning.

---

## Future Enhancements
- **Video Classification**: Extend functionality to classify video frames.
- **Real-Time Detection**: Implement real-time classification for surveillance systems.
- **Deployment**: Host the application on platforms like AWS, Heroku, or Render.

---

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Credits
**Created by:** Charishma Barla

Special thanks to all contributors and the open-source community.

