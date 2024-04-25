import mediapipe as mp

class Vision:
    def __init__(self, model):
        self.model = model

    def predict(self, image):
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.math_model = MathModel()
        self.x = 600
        self.y = 50
        self.w = 650
        self.h = 100