# Hand Sign Detection

This project involves detecting hand signs using a Keras model trained with Teachable Machine. It includes various components such as data collection, model training, and a web-based visualization interface.

## Project Structure

### Folders

- **`images/`**: Contains image data used to train the hand sign detection model.
- **`model/`**: Contains the trained Keras model.
- **`templates/`**: Contains HTML files for the web interface hosted with Flask.

### Python Files

- **`app.py`**: Main application file using `cvZone` for hand sign detection and `Flask` for hosting a web interface.
- **`collectdata.py`**: Script for collecting data. Modify folder paths to your image directories.
- **`demo.py`**: Script for hand sign detection using `MediaPipe` as an alternative to `cvZone`.
- **`test.py`**: Similar to `app.py` but without the web interface.

## Creating and Training a Keras Model Using Teachable Machine

1. **Go to Teachable Machine**:
   - Visit [Teachable Machine](https://teachablemachine.withgoogle.com/) and start a new Image Project.

2. **Set Up Your Project**:
   - Click "Get Started" to begin a new image classification project.

3. **Import Your Images**:
   - Click "Upload" to import images of different hand signs. Organize images into classes corresponding to each hand sign you want to detect.

4. **Train Your Model**:
   - Once you have uploaded and organized your images, click "Train Model" to start the training process. Teachable Machine will process your images and create a model based on your data.

5. **Download Your Model**:
   - After training is complete, click "Export Model" and select "TensorFlow / Keras." Download the model files and place them in the `model/` directory of your project.

## Setup and Usage

### 1. Install the Necessary Libraries

Ensure you have the required libraries by running:

```bash
pip install cvzone flask numpy mediapipe
