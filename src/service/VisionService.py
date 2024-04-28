from PIL import Image
import cv2
import json
import io
import google.ai.generativelanguage as glm

class VisionService:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def generate_response_from_vision(self, model, prompt):
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            if frame is None:
                continue
            pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format='JPEG')
            blob = glm.Blob(
                mime_type='image/jpeg',
                data=img_byte_arr.getvalue()
            )
            response = model.generate_content([prompt, blob])
            response = json.loads(response.text[response.text.find("{"):response.text.find("}") + 1])
            response['answer'] = response['long_description']
            return response
