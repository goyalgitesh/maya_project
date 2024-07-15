from gtts import gTTS
import pygame
import os
import asyncio

class TextToSpeech:
    def __init__(self):
        pygame.mixer.init()

    async def speak(self, text):
        tts = await asyncio.to_thread(gTTS, text=text, lang='en')
        await asyncio.to_thread(tts.save, "temp_audio.mp3")
        pygame.mixer.music.load("temp_audio.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)
        os.remove("temp_audio.mp3")