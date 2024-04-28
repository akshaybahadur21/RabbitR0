import json
import os

import google.generativeai as genai
from src.prompt.BasePrompt import base_prompt
from src.prompt.VisionPrompt import vision_prompt
import pyttsx3

from src.service.PromptService import PromptService
from src.utils.VisionUtils import generate_response_from_vision


class GeminiService:
    def __init__(self):
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
        self.text_genai_model = genai.GenerativeModel('gemini-pro')
        self.video_genai_model = genai.GenerativeModel('gemini-pro-vision')
        self.chat = self.text_genai_model.start_chat(history=[])
        self.tts_engine = pyttsx3.init()
        self.tts_engine.setProperty('volume', 1.0)
        self.tts_engine.setProperty("rate", 178)

    def converse(self, speech):
        prompt_map = PromptService.get_prompt_map()
        base = prompt_map[base_prompt.id]
        response = self.chat.send_message(PromptService.massage_prompt(base, speech).text)
        print(response.text)
        response = json.loads(response.text[response.text.find("{"):response.text.find("}") + 1])
        processed_response = self.process_response(response)
        return processed_response

    def process_response(self, response):
        if response['intent'] == 'greeting':
            self.chat = self.text_genai_model.start_chat(history=[])
        if response['intent'] == 'image':
            self.tts_engine.say(response['answer'])
            self.tts_engine.runAndWait()
            response = generate_response_from_vision(model=self.video_genai_model, prompt=vision_prompt.text)
        print(response)
        return response
