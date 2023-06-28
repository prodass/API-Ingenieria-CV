from flask import Flask, request, jsonify
from DeteccionV3 import DeteccionV3

class APIIngenieriaCV:
    def __init__(self):
        # Crear la instancia de Flask
        self.app = Flask(__name__)

        # Configurar la ruta para el endpoint de detección de objetos
        self.app.add_url_rule('/api/detect_objects', 'detect_objects', self.detect_objects, methods=['POST'])

        # Crear una instancia de la clase DeteccionV3
        self.detector = DeteccionV3()

    def detect_objects(self):
        # Obtener la imagen enviada en la solicitud
        image = request.files['image']

        # Procesar la imagen utilizando la clase DeteccionV3
        classes = self.detector.detect_objects(image)

        # Devolver las clases detectadas como respuesta JSON
        response = {'classes': classes}
        return jsonify(response)

    def run(self, host='0.0.0.0', port=5000):
        # Ejecutar la aplicación Flask
        self.app.run(host=host, port=port)

# Crear una instancia de la clase APIIngenieriaCV y ejecutar la API
api = APIIngenieriaCV()
api.run()