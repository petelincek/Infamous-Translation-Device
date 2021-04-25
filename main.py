import googletrans
from googletrans import Translator
import speech_recognition as sr
import sys
import subprocess
import time
import os
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    #r.energy_threshold = 1500
    def Capture_speech():
        print('Speak anything: ')
        audio = r.record(source, duration=4)

        try:
            finish_var = 0
            text = r.recognize_google(audio)
            command = None
            command = format(text)
            print("**************************")
            print('TEXT: {}'.format(text))
            print("**************************")

            translator=Translator()
            result=translator.translate(command,src="en",dest="de")
            print("TRANSLATING TEXT FROM {} TO {}:".format(result.src, result.dest))
            print(result.text)
            print("\n")
            time.sleep(5)
            Capture_speech()

        except:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print('Sorry did not get that!')
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
            time.sleep(5)
            Capture_speech()

    Capture_speech()