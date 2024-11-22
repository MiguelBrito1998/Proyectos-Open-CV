#Operadores Bitwise and-or-not-xor
import cv2
import numpy as np 

img1=np.zeros((400,600),dtype=np.uint8)
img1[100:300,200:400]=255
img2=np.zeros((400,600),dtype=np.uint8)
img2=cv2.circle(img2,(300,200),125,(255),-1)

AND=cv2.bitwise_and(img1,img2)
cv2.imshow("AND",AND)
OR=cv2.bitwise_or(img1,img2)
cv2.imshow("Or",OR)
NOT=cv2.bitwise_not(img1)   #solo se necesita una imagen, invierte los colores
cv2.imshow("NOT",NOT)
XOR=cv2.bitwise_xor(img1,img2)
cv2.imshow("XOR",XOR)
#podemos usar bitwise para poder visualizar partes de nuestras imagenes
# cv2.imshow('Imagen 1',img1)
# cv2.imshow('Imagen 2 ', img2)

if cv2.waitKey(0) and 0xFF==ord('s'):
    cv2.destroyAllWindows()
