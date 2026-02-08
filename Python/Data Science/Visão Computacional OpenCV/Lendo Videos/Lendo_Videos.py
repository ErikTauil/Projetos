import cv2

# Função VideoCapture
cap = cv2.VideoCapture ('assets/videos/dog.mp4')

while True:
    _, frame  = cap.read()

    cv2.imshow('video do dog', frame)

    # WaitKey para vídeos
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break

    # (-215 assertion failed)

cap.release()
cv2.destroyAllWindows()