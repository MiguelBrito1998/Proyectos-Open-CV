import cv2

captura=cv2.VideoCapture("Miguel.mp4")   #conectar la camara de la laptop

while(captura.isOpened()): #nos permite leer la imagen a cada momento
    ret,imagen=captura.read()   #ret devuelve un valor booleano (True or False)  False cuando no se ha inicializado la imagen
    if ret==True:
        cv2.imshow('Video',imagen)  #dentro del parentesis solo es el titulo de la ventana
        # salida.write(imagen)
        if cv2.waitKey(100) & 0xFF==ord('s'):
            break
    else:
        break

captura.release()  #Finalizar la captura
cv2.destroyAllWindows()