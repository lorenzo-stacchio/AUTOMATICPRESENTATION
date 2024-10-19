from gtts import gTTS
import os
from TTS.api import TTS
from enum import Enum

class SyntheticAudioTypes(Enum):
    google_tts = 0,
    tts_coqui = 1,
    #google_tts = 2    

def generate_audio(text, filename, method:SyntheticAudioTypes):
    if method == SyntheticAudioTypes.google_tts:
        filename += ".mp3"
        # Generate TTS
        tts = gTTS(text=text, lang='en')
        # Save the audio to a file
        tts.save(f"{filename}")
    elif method == SyntheticAudioTypes.tts_coqui:
        ## samples from VTK dataset used in tts arehere: https://github.com/CorentinJ/Real-Time-Voice-Cloning/tree/master/samples
        filename += ".wav"
        tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False, gpu=True)
        # List available speakers if the model supports multi-speaker output
        speakers = tts.speakers
        print("Available speakers:", speakers)
        # exit()
        # Select a male speaker by name or index if available
        # You can manually check the list of speakers and choose a male one
        selected_speaker = "p226"  # Example: 'p225' is a male speaker in the VCTK dataset
        # Text to synthesize
        # text = "Hello! This is an example of a male voice using Coqui TTS."
        # Run TTS
        tts.tts_to_file(text=text, speaker=selected_speaker, file_path=filename)
    else:
        raise Exception("Not implemented voice generator.")
    
    return filename