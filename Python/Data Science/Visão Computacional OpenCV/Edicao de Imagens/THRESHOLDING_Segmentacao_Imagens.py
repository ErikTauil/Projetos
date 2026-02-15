import cv2

# Thresholding = técnica de segmentação de imagem que converte uma imagem colorida ou em tons de cinza em uma imagem binária (preto e branco)
# Se o pixel for mais escuro que o corte, ele vira preto.
# Se o pixel for mais claro que o corte, ele vira branco.



img = cv2.imread('assets/fotos/cats.jpg')
cv2.imshow('Gatinhos', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gatinhos em tom de cinza', gray)

# THRESHOLDING Simples
thresholding, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholing simples', thresh)


# THRESHOLDING Simples Invertido
thresholding, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Thresholing simples Invertido', thresh_inv)

# Adaptative THRESHOLDING
adaptive_thresh_gaussian = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 9)
adaptive_thresh_mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 9)
cv2.imshow('adaptive thresh gaussian', adaptive_thresh_gaussian)
cv2.imshow('adaptive thresh mean', adaptive_thresh_mean)

cv2.waitKey(0)