#espacio de color HSV
import cv2
import numpy as np 

cap=cv2.VideoCapture(0)

redbajo1=np.array([0,100,20],np.uint8)
redalto1=np.array([0,255,255],np.uint8)

redbajo2=np.array([175,100,20],np.uint8)
redalto2=np.array([179,255,255],np.uint8)

while True:
    ret, frame = cap.read()
    if ret==True:
        frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)   #transformar de BGR a HSV
        maskRed1=cv2.inRange(frameHSV,redbajo1,redalto1)
        maskRed2=cv2.inRange(frameHSV,redbajo2,redalto2)
        maskRed=cv2.add(maskRed1,maskRed2)
        maskRedVeis=cv2.bitwise_and(frame,frame,mask=maskRed)

        cv2.imshow('Mascaraveis',maskRedVeis)
        cv2.imshow('Mascara roja', maskRed)
        cv2.imshow('Video',frame)
        if cv2.waitKey(1) and 0xFF==ord('s'):
            break
cap.release()
cv2.destroyAllwindows()
