import cv2
import numpy as np

imagen=cv2.imread(r'C:\Users\USUARIO\Desktop\PythonSiddhardhan\Multimedia\contorno.jpg.jpeg')
gray=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,th=cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

contornos,hierarchy=cv2.findContours(th,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen,contornos,2,(0,255,0),3)

# print(contornos)
print(hierarchy)




#El -1 significa que se dibujaran todos los contornos encontrados por el algoritmo

# for i in range(len(contornos)):
#     cv2.drawContours(imagen,contornos,i,(0,255,0),3)
#     cv2.imshow('imagen',imagen)
#     cv2.waitKey(0)


# cv2.imshow('th',th)
# cv2.imshow('imagen', imagen)
# cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()