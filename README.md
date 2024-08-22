**Hand Sign Detection**
This project involves detecting hand signs using a Keras model trained with Teachable Machine. The project includes various components such as data collection, model training, and web-based visualization. Below is an overview of how to set up and use the project.

**Project Structure**
	├── images/
	│   ├── (Your image data for training the model)
	├── model/
	│   ├── (Your trained Keras model)
	├── templates/
	│   ├── (HTML files for the web interface)
	├── app.py
	├── collectdata.py
	├── demo.py
	├── test.py
	├── README.md

**Folders:**
	images/: Contains image data used to train the hand sign detection model.
	model/: Contains the trained Keras model.
	templates/: Contains HTML files for the web interface hosted with Flask.

**Python Files:**
	app.py: Main application file using cvZone for hand sign detection and Flask for hosting a web interface.
	collectdata.py: Script for collecting data. Modify folder paths to your image directories
	demo.py: Script for hand sign detection using MediaPipe as an alternative to cvZone.
	test.py: Similar to app.py but without the web interface.

**Creating and Training a Keras Model Using Teachable Machine**
	1.Go to Teachable Machine:
	2.Visit Teachable Machine Image Project.
	3.Set Up Your Project:
	4.Click "Get Started" to begin a new image classification project.
	5.Import Your Images:
	6.Click "Upload" to import images of different hand signs. You can organize images into classes corresponding to each hand sign you want to detect.
	7.Train Your Model:
	8.Once you have uploaded and organized your images, click "Train Model" to start the training process. Teachable Machine will process your images and create a model based on your data.
	9.Download Your Model:
	10.After training is complete, click "Export Model" and select "TensorFlow / Keras." Download the model files and place them in the model/ directory of your project.
	11.Setup and Usage

**Install the necessary libraries:**
pip install cvzone flask numpy mediapipe
Collect Data:
Use collectdata.py to collect additional data if needed. Adjust the paths in this script to your directories.

Train the Model:
If you have used Teachable Machine, place the downloaded Keras model files into the model/ directory.

**Run the Application:**
Start the Flask application with:
	python app.py
	Access the web interface to visualize hand sign detection.

Test Without Web Interface:
Use test.py to test the model in a command-line environment:
	python test.py

Demo with MediaPipe:
For a demo using MediaPipe for hand sign detection:
	python demo.py

**Notes**
Ensure the paths in collectdata.py and other scripts are correctly set to your project directories.
Customize the web interface by editing the HTML files in templates/.
The model downloaded from Teachable Machine should be placed in the model/ folder before running app.py or test.py.

**Conclusion**
This project enables hand sign detection with a Keras model trained using Teachable Machine and offers a web interface for visualization. Follow the steps to set up your environment, train your model, and test the detection system.
