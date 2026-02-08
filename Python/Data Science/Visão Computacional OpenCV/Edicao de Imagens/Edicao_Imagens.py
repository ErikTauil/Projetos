import cv2
import numpy as np

# Lendo a imagem - 3 channels
img = cv2.imread('assets/fotos/cat.jpg')
img2 = cv2.imread('assets/fotos/park.jpg')


# 1. Converter imagem para Preto e Branco P&B (grayscale ou greyscale)
cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gato', img)
cv2.imshow('gato cinza', cinza)

# 2. Blur (borrar imagens)
# cv2.GaussianBlur (imagem, ksize, sigmaX)
blurred = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
cv2.imshow('blurred', blurred)

# 3. Edge Cascade - detecção de borda
# cv2.Canny(imagem, threshold1, threshold2) 
canny = cv2.Canny(img, 250, 200)
cv2.imshow('canny1', canny)

canny_blurred = cv2.Canny(blurred, 250, 200)
cv2.imshow('cammy blurred', canny_blurred)

# 4. Dilating Imagem - Dilatação de Imagem
dilatada = cv2.dilate(canny_blurred, (9,9), iterations=3)
cv2.imshow('dilatada', dilatada)

# 5. Editing Image - Correndo a imagem
eroded = cv2.erode(dilatada, (9,9), iterations=3)
cv2.imshow('eroded', eroded)

# 6. Resize
resized = cv2.resize(img, (300, 300))
cv2.imshow('resized', resized)

# 7. Crop - Cortar Imagem
corte = img[50:200, 200:400] # Corte da imagem sendo Da linha 50 até linha 200 e Da Coluna 200 até a Coluna 400
cv2.imshow('corte de matriz', corte)





cv2.waitKey(0)