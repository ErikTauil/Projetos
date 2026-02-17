import cv2
import numpy as np

img = cv2.imread('assets/fotos/park.jpg')

cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('imagem em cinza', cinza)

# Método LAPLACIANO
laplaciano = cv2.Laplacian(cinza, cv2.CV_64F)

# Calcular o valor absoluto por elemento e conveter pra unit8 (0 a 255)
laplaciano = np.uint8(np.absolute(laplaciano))
cv2.imshow('Laplaciano refatorado', laplaciano)

# MÉTODO DE SOBEL
x = cv2.Sobel(cinza, cv2.CV_64F, 1, 0)
y = cv2.Sobel(cinza, cv2.CV_64F, 0, 1)

# resultados separados das derivadas com o metodo de Sobel
cv2.imshow('Sobel X', x)
cv2.imshow('Sobel Y', y)

# Combinar x e y em uma bitwise operation
combined_sobel =cv2.bitwise_or(x,y)
cv2.imshow('Sobel combinado x+y', combined_sobel)

# MÉTODO CANNY
canny = cv2.Canny(cinza, 150,175)
cv2.imshow('Filtro Canny', canny)

cv2.waitKey(0)