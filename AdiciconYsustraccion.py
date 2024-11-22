import cv2 

img1=cv2.imread('.\multimedia\Saca.jpg',0)
img2=cv2.imread('.\Multimedia\cadena.jpg',0)
img1=cv2.resize(img1,(200,200))
img2=cv2.resize(img2,(200,200))
resA=cv2.add(img1,img2)

# print(img1[0:3,0:3])
# print(img2[0:3,0:3])
# print(resA[0:3,0:3])

# resAW=cv2.addWeighted(img1,0.3,img2,0.3,0)
# cv2.imshow('resAW',resAW)

# cv2.imshow("Suma de las imagenes",resA)
# cv2.imshow('Sacapuntas',img1)
# cv2.imshow("cadena",img2)

#sustraccion

resultado=cv2.subtract(img1,img2)
resultado2=cv2.absdiff(img1,img2)


print(img1[0:3,0:3])
print(img2[0:3,0:3])
print(resultado[0:3,0:3])
print(resultado2[0:3,0:3])

cv2.imshow('resultado1',resultado)
cv2.imshow('resultado2',resultado2)
cv2.waitKey()
cv2.destroyAllWindows