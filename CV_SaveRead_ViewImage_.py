import cv2

imagen=cv2.imread('.\heisenberg.jpg',0)  #el cero lleva la imagen a escala de grises 
nuevo=(800,400)
imagen=cv2.resize(imagen,nuevo)
cv2.imshow('Heisenberg',imagen)   #muestra la imagen
cv2.imwrite('OtraFOTO.jpg',imagen)
cv2.waitKey(0)      #clave para esperar que se ingrese una tecla
cv2.destroyAllWindows()    #cerrar todas las ventanas