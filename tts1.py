#!/usr/bin/python3

#importing gtts module which uses google API for tts conversion

from gtts import gTTS
import os
inputt = input("Enter your text")
tts = gTTS(text=inputt, lang='en')
tts.save("audio.mp3")
os.system("mpg321 audio.mp3")
