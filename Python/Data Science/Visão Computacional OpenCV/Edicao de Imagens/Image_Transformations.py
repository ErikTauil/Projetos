import cv2
import numpy as np

img = cv2.imread('assets/fotos/park.jpg')
cv2.imshow('imagem normal', img)



# 1  Definições de funções - Imagem Transaladada
def translate(img, x, y):
    """
    -x  ESQUERDA
    -y  ACIMA
    x  DIREITA
    y  ABAIXO
    """
    translation_matrix = np.float32([[1,0,x],[0,1,y]])

    # coletamos as dimensões da nossa imagem
    dimensions = (img.shape[1], img.shape[0])
    #retornar a função warpAffine
    return cv2.warpAffine(img, translation_matrix, dimensions)

img_tr = translate(img, 100, 250)
cv2.imshow('transladada', img_tr)

# 2 Rotação da Imagem
def rotate(img, angle, rotation_point=None):
    height, width = img.shape[:2]

    if rotation_point is None:
        rotation_point = (width//2, height//2)

    # get matriz de rotação 2d (ponto_de_rotação,angulo,escala)
    rotation_matrix = cv2.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotation_matrix, dimensions)

rotacionada = rotate(img, -45)
cv2.imshow('Imagem Rotacionada', rotacionada)

# 3 Imagem Flipping - Inverte um array 2D
flip1 = cv2.flip(img, 1) # horizontal
flip2 = cv2.flip(img, 0) # vertical
flip3 = cv2.flip(img,-1) # vertical e horizontal
cv2.imshow('Flipadas Horizontal', flip1)
cv2.imshow('Flipadas vertical', flip2)
cv2.imshow('Flipadas vertical e horizontal', flip3)


# 4 Resizing 
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('resize', resized)

# 5 Cropping
# Garante que o crop está dentro da imagem
h, w = img.shape[:2]
y1, y2 = 100, min(400, h)
x1, x2 = 200, min(500, w)

cropped = img[y1:y2, x1:x2]

if cropped.size == 0:
    print("Crop inválido - fora dos limites da imagem")
else:
    cv2.imshow('crop', cropped)


cv2.waitKey(0)