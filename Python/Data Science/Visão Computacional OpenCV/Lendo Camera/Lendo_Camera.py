import cv2
import numpy as np

# Objeto de Captura
cap = cv2.VideoCapture(0)

while True:
    # coletar o frame

    _, frame = cap.read()

    cv2.imshow('Gravação Camera Erik', frame) 

    # adicionar opção para sair do loop
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break