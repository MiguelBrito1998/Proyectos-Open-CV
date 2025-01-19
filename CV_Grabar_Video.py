import cv2

captura=cv2.VideoCapture(0)   #conectar la camara de la laptop
salida = cv2.VideoWriter('Video.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 20.0, (640, 480)) #FPS es el 20 y el arreglo es el tamaño de la imagen
while(captura.isOpened()): #nos permite leer la imagen a cada momento
    ret,imagen=captura.read()   #ret devuelve un valor booleano (True or False)  False cuando no se ha inicializado la imagen
    if ret==True:
        cv2.imshow('video',imagen)  #dentro del parentesis solo es el titulo de la ventana
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF==ord('s'):
            break

captura.release()  #Finalizar la captura
salida.release()   #Salida de la grabacion
cv2.destroyAllWindows()   #Cerrar todas las ventanas