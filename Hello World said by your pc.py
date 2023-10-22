import pyttsx3  #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
#for female [1]


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Gooood Morning!")

    elif hour>=12 and hour<18:
        speak("Gooood Afternoon!")

    else:
        speak("Gooood Evening!")

    speak("hello mam i am your friend siya . Please tell me how may I help you")
#
