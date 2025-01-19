import cv2
import numpy as np
import imutils

image=cv2.imread('C:/Users/USUARIO/Desktop/PythonSiddhardhan/Multimedia/kill.jpg')
image=cv2.resize(image,(500,200),interpolation=cv2.INTER_CUBIC)
ancho=image.shape[1]  #columnas
alto=image.shape[0]  #filas

# traslacion
M=np.float32([[1,0,10],[0,1,11]])   #10 espacios a la derecha y 100 hacia abajo, lo mismo podemos hacer con valore negativos
imageOut1=cv2.warpAffine(image,M,(ancho-200,alto-200))

# Rotamos la imagen
M=cv2.getRotationMatrix2D((ancho//2,alto//2),180,1)  # el tercer parametro indica el acercamiento y alejamiento
imageOut2=cv2.warpAffine(image,M,(ancho,alto))

# Resize una imagen con imutils
imageOut3=imutils.resize(image,height=500)

#recortando una imagen
print('image.shape=',image.shape)
imageOut4=image[100:200,250:500]






# cv2.imshow('Imagen de entrada', image)
cv2.imshow("imagen original",image)
cv2.imshow('Imagen de salida1',imageOut1)
cv2.imshow('Imagen de salida2',imageOut2)
cv2.imshow('Imagen de salida3',imageOut3)
cv2.imshow('Imagen de salida4',imageOut4)


# cv2.imshow("Black panther", image)
cv2.waitKey(0)
cv2.destroyAllWindows()