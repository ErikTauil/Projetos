import cv2
import numpy as np

# criar um canva completamente preto
blank = np.zeros([400,400], dtype='uint8')
cv2.imshow('blank', blank)

rectangle = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

cv2.imshow('Ret', rectangle)
cv2.imshow('Circ', circle)

# Bitwise AND -> a intersecção das duas imagens (ambos são 1 [brancos])
bitwise_and = cv2.bitwise_and(rectangle,circle)
cv2.imshow('and - Interseccao das duas imagens', bitwise_and)

# Bitwise OR -> a intersecção onde há qualquer um dos dois objetos envolvidos
bitwise_or = cv2.bitwise_or(rectangle,circle)
cv2.imshow('OR - Interseccao das duas imagens', bitwise_or)

# Bitwise XOR -> a intersecção apenas nas áreas onde há UM OU OUTRO
bitwise_xor = cv2.bitwise_xor(rectangle,circle)
cv2.imshow('XOR - Interseccao das duas imagens', bitwise_xor)


# Bitwise NOT -> a intersecção apenas onde não há nada (0)
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow('Circle NOT', bitwise_not)

cv2.waitKey(0)