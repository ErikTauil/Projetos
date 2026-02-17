import cv2
import mediapipe as mp
import numpy as np
import time

# Para funcionar usar a versão Python 3.10.11 e
#  No Terminal digitar:
# pip uninstall mediapipe -y
# pip install mediapipe==0.10.11


# Tipagem (opcional)
confidence = float
webcam_image = np.ndarray
rgb_tuple: tuple[int, int, int]

# Classe ===================================

class Detector:
    def __init__(self,
                model: bool = False,
                number_hands: int = 2,
                model_complexity: int = 1,
                min_detec_confidence: float = 0.5,
                min_tracking_confidence: float = 0.5):
        # Parâmetros necessários para inicializar o Hands
        self.mode = model
        self.max_num_hands = number_hands
        self.complexity = model_complexity
        self.detection_con = min_detec_confidence
        self.tracking_con = min_tracking_confidence

        # Inicializar o Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.max_num_hands,
                                        model_complexity=self.complexity,
                                        min_detection_confidence=self.detection_con,
                                        min_tracking_confidence=self.tracking_con)
        self.mp_draw = mp.solutions.drawing_utils
        self.tip_ids = [4, 8, 12, 16, 20]  # Pontas dos dedos

        self.results = None
        self.required_landmark_list = []

    def find_hands(self,
                img: webcam_image,
                draw_hands: bool = True):
        # Correção de cor
        img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Coletar resultados do processo das hands e analisar
        self.results = self.hands.process(img_RGB)

        if self.results.multi_hand_landmarks and draw_hands:
            for hand in self.results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(img, hand, self.mp_hands.HAND_CONNECTIONS)  

        return img

    def find_position(self,
                    img: webcam_image,
                    hand_number: int = 0):        
        self.required_landmark_list = []

        if self.results and self.results.multi_hand_landmarks:
            height, width, _ = img.shape
            my_hand = self.results.multi_hand_landmarks[hand_number]  # qual mão

            for id, lm in enumerate(my_hand.landmark):
                center_x, center_y = int(lm.x * width), int(lm.y * height)
                self.required_landmark_list.append([id, center_x, center_y])

        return self.required_landmark_list

# Teste de Classe =================
if __name__ == '__main__':
    previous_time = 0
    
    # Inicializa detector
    Detec = Detector()

    # Captura de vídeo
    capture = cv2.VideoCapture(0)

    while True:
        success, img = capture.read()
        if not success:
            print("Falha ao capturar o vídeo")
            break

        # Manipulação de frame
        img = Detec.find_hands(img)
        landmark_list = Detec.find_position(img)
        if landmark_list:
            # Ponta do dedo indicador (id 8)
            print(landmark_list[8])

        # Calculando FPS
        current_time = time.time()
        fps = 1 / (current_time - previous_time) if previous_time != 0 else 0
        previous_time = current_time

        # Mostrando FPS na tela
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 255), 3)
        cv2.imshow('Camera do Erik Tauil', img)

        # Sair com 'q'
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
