import cv2
import numpy as np
from .model import FacialRecognitionModel

class FacialRecognitionSystem:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.model = FacialRecognitionModel()

    def detect_face(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        return faces

    def recognize_face(self, face_image):
        face_image = cv2.resize(face_image, (128, 128))
        face_image = np.expand_dims(face_image, axis=0)
        prediction = self.model.predict(face_image)
        return prediction

    async def process_image(self, image_path):
        image = cv2.imread(image_path)
        faces = self.detect_face(image)
        results = []
        for (x, y, w, h) in faces:
            face = image[y:y+h, x:x+w]
            identity = await self.recognize_face(face)
            results.append({"bbox": (x, y, w, h), "identity": identity})
        return results

    async def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            faces = await self.process_image(frame)
            for face in faces:
                (x, y, w, h) = face['bbox']
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                cv2.putText(frame, face['identity'], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            cv2.imshow('Facial Recognition', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()