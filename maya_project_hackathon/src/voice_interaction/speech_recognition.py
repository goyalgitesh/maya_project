import speech_recognition as sr
import asyncio

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    async def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = await asyncio.to_thread(self.recognizer.listen, source)
        try:
            return await asyncio.to_thread(self.recognizer.recognize_google, audio)
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError:
            return "Could not request results from the speech recognition service"