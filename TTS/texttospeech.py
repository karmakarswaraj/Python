# import win32com.client
# youtuber = win32com.client.Dispatch("SAPI.SpVoice")
# viewrs = ['HARRY', 'NISCHAY', 'JAYUUU', 'DIMPLE', "ABHISHEK", "VINAY"]
# for name in viewrs:
#     youtuber.Speak(f'SHOUTOUT TO {name} FOR WATCHING MY VIDEOS!')



from gtts import gTTS
import os

# Text to be converted to speech
viewrs = ['HARRY', 'NISCHAY', 'JAYUUU', 'DIMPLE', "ABHISHEK", "VINAY"]

for name in viewrs:
    tts = gTTS(name)  # Initialize the gTTS object with the current name
    audio_file = f"{name}.mp3"  # Create a unique audio file name for each name
    tts.save(audio_file)

    # Play the speech using a system player (e.g., VLC or mpg321)
    os.system(f"mpg321 {audio_file}")  # This is for Linux, use a different player for other platforms if needed