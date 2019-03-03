from gtts import gTTS
import os

def write(txt:str):    
    tts = gTTS(text=txt, lang='en')
    tts.save("ttsoutput.mp3")

def play():
    os.system("mpg321 ttsoutput.mp3")