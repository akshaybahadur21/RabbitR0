# import mediapipe as mp
import cv2


class VisionService:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def process_video(self):
        ret, frame = self.cap.read()
        while ret:
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
