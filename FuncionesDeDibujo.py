import cv2
import numpy as np

imagen=50*np.ones((400,600,3),dtype=np.uint8)

#dibujando la linea

cv2.line(imagen,(0,0),(600,400),(250,50,250),4)

cv2.rectangle(imagen,(50,50),(300,300),(0,0,255),10)
cv2.circle(imagen,(50,50),100,(0,255,0),-1)

font=cv2.FONT_HERSHEY_SIMPLEX

a=30
for i in range(8):
    a+=30
    cv2.putText(imagen,'Soy Miguel Brito',(10,a),i,1,(0,255,255),2,cv2.LINE_AA)


cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()