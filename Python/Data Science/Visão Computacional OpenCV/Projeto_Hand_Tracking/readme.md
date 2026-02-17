# Hand Tracking com OpenCV e MediaPipe

## Descrição do Projeto

Este projeto realiza **detecção e rastreamento das mãos em tempo real** utilizando a biblioteca **MediaPipe** junto com **OpenCV**. 
A aplicação captura vídeo da webcam, detecta os pontos-chave da mão (landmarks), identifica a posição de cada dedo e exibe o **FPS (frames por segundo)** em tempo real.

O objetivo é criar uma base para futuros projetos de **interação com gestos**, reconhecimento de sinais ou controle de interfaces por gestos.

> No vídeo de demonstração, as mãos que aparecem são do filho do autor, participando de forma divertida do teste do sistema.  

---

## Funcionalidades

- Detecta até 2 mãos simultaneamente.  
- Rastreia os **21 pontos-chave** de cada mão.  
- Mostra a **posição do dedo indicador** no terminal.  
- Calcula e exibe o **FPS** em tempo real.  
- Estrutura modular com a classe `Detector` para facilitar reutilização do código.  

---

## Tecnologias e Bibliotecas Utilizadas

- **Linguagem:** Python 3.10  
- **Bibliotecas:**
  - [OpenCV](https://opencv.org/) — captura e manipulação de vídeo.  
  - [MediaPipe](https://developers.google.com/mediapipe) — detecção e rastreamento de mãos.  
  - [NumPy](https://numpy.org/) — manipulação de arrays e coordenadas.  
  - [time](https://docs.python.org/3/library/time.html) — cálculo de FPS.

---

## Como Executar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/hand-tracking.git

