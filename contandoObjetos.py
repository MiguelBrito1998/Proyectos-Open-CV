import cv2

imagen=cv2.imread('C:/Users/USUARIO/Desktop/PythonSiddhardhan/Multimedia/monedas.jpg')
grises=cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

_,th=cv2.threshold(grises,240,255,cv2.THRESH_BINARY_INV)

contornos,_=cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(imagen,contornos,-1,(255,0,0),2)


print('numero de contorns',len(contornos))

# cv2.imshow('Monedas',imagen)
# cv2.imshow('Monedas Escala de grises',th)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

for c in contornos:
    cv2.drawContours(imagen,[c],0,(255,0,0),2)
    cv2.imshow("Imagen",imagen)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()