import cv2 
import numpy as np 
import imutils 

image=cv2.imread('./Multimedia/Saca.jpg',0)
image=imutils.resize(image,width=400)

_,binarizada=cv2.threshold(image,210,255,cv2.THRESH_BINARY)
_,binarizadaInv=cv2.threshold(image,210,255,cv2.THRESH_BINARY_INV)
_,trunc=cv2.threshold(image,255,255,cv2.THRESH_TRUNC)
_,tozero=cv2.threshold(image,210,255,cv2.THRESH_TOZERO)
_,tozero_inv=cv2.threshold(image,210,255,cv2.THRESH_TOZERO_INV)


# el tercer parametro de la ufncin threshold es nulo, no se toma en cuenta a la hora de mostrar la imagen

# cv2.imshow('Imagen normal', image)
# cv2.imshow('Imagen binarizada',np.hstack([binarizada,binarizadaInv]))
# cv2.imshow('Imagen truncada',trunc)
cv2.imshow('Imagen tozero',np.hstack([tozero,tozero_inv]))
cv2.imshow("Imagen de sacapuntas",image)
cv2.waitKey(0)
cv2.destroyAllwindows()

