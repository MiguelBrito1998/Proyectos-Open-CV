import numpy as np
import cv2

def dibujar(mask,color):
    contornos, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area=cv2.contourArea(c)
        if area>300:
            M=cv2.moments(c)
            if (M["m00"]==0) : M["m00"]=1
            x=int(M["m10"]/M['m00'])
            y=int(M['m01']/M['m00'])
            cv2.circle(frame,(x,y),7,(0,255,0),-1)
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,'{},{}'.format(x,y),(x+10,y),font,0.75,3)
            nuevoContorno=cv2.convexHull(c)   #suavizado de los bordes del area del contornos
            cv2.drawContours(frame,[nuevoContorno],0,color,3)
        # cv2.imshow('maskazul',mask)


cap=cv2.VideoCapture(0)

azulBajo=np.array([100,100,20],np.uint8)
azulAlto=np.array([125,255,255],np.uint8)

amarilloBajo=np.array([15,100,20],np.uint8)
amarilloAlto=np.array([45,255,255],np.uint8)

rojoBajo=np.array([0,100,20],np.uint8)
rojoAlto=np.array([5,255,255],np.uint8)

rojobajo2=np.array([175,100,20],np.uint8)
rojoalto2=np.array([179,255,255],np.uint8)

while True:
    ret,frame=cap.read()
    if ret==True:
        frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskAmarillo=cv2.inRange(frameHSV,amarilloBajo,amarilloAlto)
        maskRoja1=cv2.inRange(frameHSV,rojoBajo,rojoAlto)
        maskRoja2=cv2.inRange(frameHSV,rojobajo2,rojoalto2)
        maskAzul=cv2.inRange(frameHSV,azulBajo,azulAlto)
        maskRed=cv2.add(maskRoja1,maskRoja2)
        dibujar(maskAzul,(255,0,0))
        dibujar(maskAmarillo,(0,255,255))
        dibujar(maskRed,(0,0,255))
        cv2.imshow("imagen normal", frame)
        if cv2.waitKey(1) & 0xFF==ord('s'):
            break

cap.release()
cv2.destroyAllWindows()

