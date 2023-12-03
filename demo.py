import mediapipe as mp
import cv2
import numpy as np
import uuid
import os
import math

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

offset = 20
imgSize = 300

folder = "Image/C" 
counter = 0

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands: 
    while cap.isOpened():
        ret, frame = cap.read()
        
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        image = cv2.flip(image, 1)
        
        image.flags.writeable = False
        
        results = hands.process(image)
        
        image.flags.writeable = True
        
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        print(results)
        
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(29, 225, 76), thickness=2, circle_radius=4),
                                        mp_drawing.DrawingSpec(color=(250, 44, 23), thickness=2, circle_radius=2),
                                         )
                bbox = cv2.boundingRect(np.array([[int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])] for landmark in hand.landmark]))
                cv2.rectangle(image, (int(bbox[0]), int(bbox[1])),
                              (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])), (0, 255, 0), 2)
                imgWhite = np.ones((imgSize, imgSize,3), np.uint8)+255
                x, y, w, h = bbox
                w, h = max(w, 1), max(h, 1)

                # Adjust bounding box dimensions to capture the entire hand
                x = max(x - offset, 0)
                y = max(y - offset, 0)
                w = min(w + 2 * offset, frame.shape[1] + x)
                h = min(h + 2 * offset, frame.shape[0] + y)

                imgCrop = frame[y:y + w, x:x + h]

                imgCropShape = imgCrop.shape

                aspectRatio = h/w

                if aspectRatio > 1:
                    k = imgSize/h
                    wCal = math.ceil(k * w)
                    imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                    imgResizeShape = imgResize.shape
                    wGap = math.ceil((imgSize - wCal)/2)
                    imgWhite[:, wGap:wCal+wGap] = imgResize
                else:
                    k = imgSize/w 
                    hCal = math.ceil(k * h)
                    imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                    imgResizeShape = imgResize.shape
                    hGap = math.ceil((imgSize - hCal)/2)
                    imgWhite[hGap:hCal + hGap, :] = imgResize

                cv2.imshow("ImageCrop", imgCrop)
                cv2.imshow("ImageWhite", imgWhite)
                    
            
        cv2.imwrite(os.path.join('Output Images', '{}.jpg'.format(uuid.uuid1())), image)
        cv2.imshow('Hand Tracking', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
