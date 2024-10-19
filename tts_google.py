from gtts import gTTS
import os

from TTS.api import TTS

from Typ

def generate_audio(text, filename, method=):
    # Generate TTS
    tts = gTTS(text=text, lang='en')

    # Save the audio to a file
    tts.save(f"{filename}")