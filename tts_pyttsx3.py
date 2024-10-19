import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# List all available voices
voices = engine.getProperty('voices')
for voice in voices:
    print(f"Voice ID: {voice.id}, Name: {voice.name}")

# for voice in voices:
#     if "male" in voice.name.lower():  # You can adjust this condition to fit the voice names available on your system
#         engine.setProperty('voice', voice.id)
#         break
    
# Set a specific voice
engine.setProperty('voice', voices[0].id)  # Change index as needed to select a voice

# Speak the text
# engine.say("This is an example of a different voice.")
# engine.runAndWait()
