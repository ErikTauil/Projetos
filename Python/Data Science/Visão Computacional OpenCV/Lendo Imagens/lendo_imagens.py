import cv2

# Função imread()
img =  cv2.imread('assets/fotos/cat.jpg')
img_grande = cv2.imread('assets/fotos/cat_large.jpg')

# Função imshow()
cv2.imshow('Janela do Gato', img)
cv2.imshow('Janela Grande do Gato', img_grande)

# Função waitkey()
cv2.waitKey(0)