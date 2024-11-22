import cv2 
import numpy as np 

captura=cv2.VideoCapture(0)
mask=np.zeros((480,640),dtype=np.uint8)
mask=cv2.circle(mask,(320,240),125,(255),-1)
mask=cv2.bitwise_not(mask)
while(captura.isOpened()):
    ret,frame=captura.read()
    if ret==True:
        imgMask=cv2.bitwise_and(frame,frame,mask=mask)
        cv2.imshow("VIDEO",imgMask)

        if cv2.waitKey(1) and 0xFF==ord('s'):
            break
    else: break

captura.release()
cv2.destroyAllWindows()