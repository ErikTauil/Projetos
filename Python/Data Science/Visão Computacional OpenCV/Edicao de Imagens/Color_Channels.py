import cv2
import numpy as np

img = cv2.imread('assets/fotos/park.jpg')
cv2.imshow('Fim de semana no Parque', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


b, g, r = cv2.split(img)
cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)

# reintegrando os canais de cores
blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

cv2.imshow('Blue_2', blue)
cv2.imshow('Green_2', green)
cv2.imshow('Red_2', red)

# reintegrando a Imagem
merged = cv2.merge([b, g, r])
cv2.imshow('merged image', merged)

# Visualizar resultado no TERMINAL
print(merged.shape)

# Visualizar resultado no TERMINAL
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv2.waitKey(0)