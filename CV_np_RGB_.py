import cv2 
import numpy as np

# bgr=np.zeros((300,300,3),dtype=np.uint8)
# bgr[:,:,:]=(200,200,100)

# cv2.imshow("BGR",bgr)
# cv2.waitKey(0)
# cv2.destroyAllwindows()


# De BRG a RGBj

# bgr=cv2.imread('rgb.png')
# tam=(400,440)
# bgr=cv2.resize(bgr,tam)
# C1=bgr[:,:,0]
# C2=bgr[:,:,1]
# C3=bgr[:,:,2]
# cv2.imshow('RGB',np.hstack([C1,C2,C3]))

# #transformamos a RGB
# rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
# C1=rgb[:,:,0]
# C2=rgb[:,:,1]
# C3=rgb[:,:,2]
# cv2.imshow('RGB',np.hstack([C1,C2,C3]))
# cv2.waitKey(0)
# cv2.destroyallwindows()

#ahora para transformar a escala de grises

#transformamos a RGB
bgr=cv2.imread('heisenberg.jpg')
bgr=cv2.resize(bgr,(800,400))
gris=cv2.cvtColor(bgr,cv2.COLOR_BGR2GRAY)
cv2.imshow('GRISES',gris)
cv2.waitKey(0)
cv2.destroyAllwindows()