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
  pip install cvzone flask numpy mediapipe

### 2. Collect Data

  Use collectdata.py to collect additional data if needed. Adjust the paths in this script to match your directories.

### 3. Train the Model

  If you have used Teachable Machine, place the downloaded Keras model files into the model/ directory.

### 4. Run the Application

Start the Flask application with:
  python app.py
  Access the web interface to visualize hand sign detection by navigating to http://localhost:5000 in your web browser.

### 5. Test Without Web Interface

To test the model in a command-line environment, run:
  python test.py

### 6. Demo with MediaPipe

For a demo using MediaPipe for hand sign detection, run:
  python demo.py

Ensure the paths in collectdata.py and other scripts are correctly set to your project directories.
Customize the web interface by editing the HTML files in the templates/ folder.
The model downloaded from Teachable Machine should be placed in the model/ folder before running app.py or test.py.

### Conclusion

This project enables hand sign detection with a Keras model trained using Teachable Machine and offers a web interface for visualization. Follow the steps to set up your environment, train your model, and test the detection system.