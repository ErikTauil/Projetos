import cv2
import numpy as np

# Cores -> BGR e Não RGB
azul = 255, 0, 0
verde = 0, 255, 0
vermelho = 0, 0, 255


# Ler as Imagens 
blank_img = np.zeros((500, 500, 3), dtype='uint8') 

cat = cv2.imread('assets/fotos/cat.jpg')

# 1. Pintando blank por operação matricial
# pintar toda a matriz
# blank_img[:] = vermelho
# blank_img[:] = azul
# blank_img[:] = verde

# Pintando uma parte específica
# blank_img[200:300, 300:400] = vermelho
# blank_img[:100, 50:150] = verde
# blank_img[400:, 200:300] = azul


# 2. Desenhando um retângulo
# cv2.rectangle(blank_img, (10,10), (250,250), verde, -1)
# cv2.rectangle(blank_img, (10,10), (250,250), verde, 6)
# cv2.rectangle(blank_img, (30,30), (blank_img.shape[1]//2, blank_img.shape[0]//2), verde, 3)


# 3. Desenhando um Circulo
# cv2.circle(blank_img, (blank_img.shape[1]//2, blank_img.shape[0]//2), 200, azul, 5)

# 4. Desenhando uma linha
# cv2.line(blank_img, (100,100), (blank_img.shape[1], blank_img.shape[0]), verde, 2)

# 5. Escrever texto
cv2.putText(blank_img, "Erik Tauil",(3, 250), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255,255,255), 3)
cv2.putText(blank_img, "Erik Tauil",(2, 249), cv2.FONT_HERSHEY_COMPLEX, 1.5, vermelho, 3)
cv2.putText(blank_img, "Erik Tauil",(0, 247), cv2.FONT_HERSHEY_COMPLEX, 1.5, azul, 3)
cv2.imshow('blank', blank_img)

cv2.waitKey(0)