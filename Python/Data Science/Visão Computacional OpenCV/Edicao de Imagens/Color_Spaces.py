import cv2
import numpy as np

img = cv2.imread('assets/fotos/cat.jpg')
cv2.imshow('Gato Normal', img)

# BGR para Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Cinza', gray)


# BGR para HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)


# BGR para L*a*b
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('L*a*b', lab)

# BGR para RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

# LAB para BRG
lab_bgr = cv2.cvtColor(lab, cv2.COLOR_Lab2BGR)
cv2.imshow('Lab para brg', lab_bgr)

cv2.waitKey(0)
