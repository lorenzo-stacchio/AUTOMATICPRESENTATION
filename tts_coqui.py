from TTS.api import TTS

## INSTALLATION INSTRUCTIONS
## FIRST INSTALL ESPEAKEN for your system
## install --> https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md#windows
## pip install espeakng
## https://github.com/idiap/coqui-ai-TTS
## pip install coqui-tts

# Initialize TTS with a pre-trained model
# You can find available pre-trained models on the Coqui TTS documentation or use the default.
# Here, we will use the "tts_models/en/ljspeech/tacotron2-DDC" model as an example.
tts = TTS(model_name="tts_models/en/vctk/vits", progress_bar=False, gpu=False)

# List available speakers if the model supports multi-speaker output
speakers = tts.speakers

# Print all available speakers to choose one
print("Available speakers:")
print(speakers)

# Select a male speaker by name or index if available
# You can manually check the list of speakers and choose a male one
selected_speaker = "p225"  # Example: 'p225' is a male speaker in the VCTK dataset

# Text to synthesize
text = "Hello! This is an example of a male voice using Coqui TTS."

# Run TTS
tts.tts_to_file(text=text, speaker=selected_speaker, file_path="male_voice_output.wav")

# The output audio is saved to "male_voice_output.wav"