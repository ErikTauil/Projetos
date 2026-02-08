import cv2
import numpy as np

cap = cv2.VideoCapture('assets/videos/dog.mp4')

# Criar função que faz o rescale para cada frame individual


def rescale_frame(frame: np.array,
                scale: float = 0.75):
    largura = int(frame.shape[1] * scale)
    altura = int(frame.shape[0] * scale)

    return cv2.resize(frame, (largura,altura), interpolation=cv2.INTER_AREA)           

def resize_frame(width: int,
                heigth: int):
    cap.set(3, width)
    cap.set(4, heigth)

# Imag