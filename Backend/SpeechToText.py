import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def transcribe_audio(self, audio_file: str) -> str:
        try:
            with sr.AudioFile(audio_file) as source:
                audio = self.recognizer.record(source)
            return self.recognizer.recognize_google(audio)
        except Exception as e:
            return f"Speech recognition failed: {str(e)}"
