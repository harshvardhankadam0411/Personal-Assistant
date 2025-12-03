import pyttsx3
import speech_recognition as sr
import os
import pywhatkit
import pyautogui

import wikipedia
import pyperclip

def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    from pyperclip import paste
    from time import sleep
    
    sleep(2)

    click(x=1137, y=261)

    hotkey('ctrl','c')

    value = pyperclip.paste()

    Link = str(value)

    def Download(link):
        url= YouTube(link)
        video.download("C:\\Users\\Aakash\\OneDrive\\Desktop\\Personal Assistant\\database\\youtube")
    
    Download(Link)
    
    speak("done sir,i have downloaded the video")

    os.startfile("C:\\Users\\Aakash\\OneDrive\\Desktop\\Personal Assistant\\database\\youtube")