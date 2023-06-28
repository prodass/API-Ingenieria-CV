import torch
import cv2
import numpy as np

class DeteccionV3:
    def __init__(self):
        # Cargar el modelo YOLOv5
        self.model = torch.hub.load('ultralytics/yolov5', 'custom',
                                    path='C:/Users/Usuario/Desktop/proyecto ing/code/bestv2.pt')

    def detect_objects(self, image):
        # Leer la imagen y convertirla a un array numpy
        img_np = np.fromfile(image, np.uint8)
        img = cv2.imdecode(img_np, cv2.IMREAD_COLOR)

        # Realizar las detecciones utilizando el modelo YOLOv5
        detect = self.model(img)

        # Obtener información de las detecciones
        info = detect.pandas().xyxy[0]  # im1 predictions

        # Filtrar detecciones con precisión mayor al 50%
        filtered_info = info[info['confidence'] > 0.5]

        # Obtener las clases de las detecciones filtradas
        classes = filtered_info['name'].unique()

        # Devolver la lista de clases detectadas
        return classes.tolist()