from flask import Flask, render_template
import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_language/Prototype1')
def gesture_recognition():
    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1)
    classifier = Classifier("D:/Ajay Programmers/sign_language/Prototype1/Model/keras_model.h5", "D:/Ajay Programmers/sign_language/Prototype1/Model/labels.txt")

    offset = 20
    imgSize = 300

    labels = ["A", "B", "C"]

    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    # Initialize index to a default value
    index = -1

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) + 255
        imgCrop = img[y - offset:y + h + offset, x:x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite)
            print(prediction, index)
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite)

        cv2.putText(imgOutput, labels[index], (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)

    cv2.imshow("Image", imgOutput)
    cv2.waitKey(1)

    # Return a response even if no hands are detected
    return {"gesture": labels[index] if index != -1 else "No hands detected"}

if __name__ == '__main__':
    app.run(debug=True)
