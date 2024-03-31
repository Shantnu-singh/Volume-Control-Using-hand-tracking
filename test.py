import mediapipe as mp
import cv2
import numpy as np
import time

import Hand_detection_module as hdm

pTime = 0
cTime = 0


cap = cv2.VideoCapture(0)
        
detector = hdm.HandDetection()


while True:
    rec , frame = cap.read()

    frame = detector.findHand(frame , flag = True)
    lmlist = detector.findPosition(frame , draw=True)
            
    if len(lmlist) != 0:
        print(lmlist[4])
            
    cTime  =time.time()
    Fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(frame , str(int(Fps)) , (10 , 40) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,255 , 0) , 2 )
            

        
    cv2.imshow("webcam" , frame)
    if cv2.waitKey(1) & 0xFF == ord("x"):
        break

cap.release()
cv2.destroyAllWindows()