from PIL import Image
import cv2
import io
import google.ai.generativelanguage as glm


def generate_response_from_vision(model, prompt):
    cap = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
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
        response['answer'] = response['short_description']
        return response
