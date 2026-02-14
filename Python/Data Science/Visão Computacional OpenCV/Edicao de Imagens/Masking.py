import cv2
import numpy as np

img = cv2.imread('assets/fotos/cats.jpg')
cv2.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow('blank', blank)


# Criar as formas 
circle = cv2.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv2.imshow('circulo', circle)
cv2.imshow('retangulo', rectangle)


# Criando Máscaras Diferentes 
recorte1 = cv2.bitwise_and(circle, rectangle)
recorte2 = cv2.bitwise_or(circle, rectangle)
recorte3 = cv2.bitwise_not(circle)


cv2.imshow('recorte 1', recorte1)
cv2.imshow('recorte 2', recorte2)
cv2.imshow('recorte 3', recorte3)

# Mostrando as máscaras
mask1 = cv2.bitwise_and(img, img, mask=recorte1)
mask2 = cv2.bitwise_or(img, img, mask=recorte2)
mask3 = cv2.bitwise_and(img, img, mask=recorte3)

cv2.imshow('mask1', mask1)
cv2.imshow('mask2', mask2)
cv2.imshow('mask3', mask3)










cv2.waitKey(0)
