import cv2
import numpy as np

# 1. Processo padrão/inicial
# Lendo a imagem que vamos trabalhar 
img = cv2.imread('assets/fotos/cats.jpg')
cv2.imshow('Cats', img)

# desenhando um canva branco do mesmo tamanho que a imagem de trabalho
blank = np.zeros(img.shape, dtype='uint8')
# cv2.imshow('Blank', blank)

# transferindo-a para cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', gray)

# 2. Deteção de Contornos

# a. Borrar a imagem  com o  GaussianBlur
blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

# b. Função de Canny
canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Canny', canny)

# Modo de detecção e Método de Aproximação

contornos, hier = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contornos)} contornos foram encontrados!')

cv2.drawContours(blank, contornos, -1, (0,0,255),1)
cv2.imshow('Contornos desenhados', blank)

cv2.waitKey(0)