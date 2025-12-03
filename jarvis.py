import pyttsx3
import speech_recognition as sr
import os

import datetime
import cv2
import random
from playsound import playsound 
import wikipedia 
from requests import get
import webbrowser
import sys
import pywhatkit as kit

import time
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate',200)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to convert voice into text
def Takecommand(): 
    r= sr.Recognizer()
    with sr.Microphone() as source:
      print("listening...")
      r.pause_threshold = 1
     
      audio = r.listen(source,timeout=15,phrase_time_limit=15)


    try:
       print("Recognizing...")
       query = r.recognize_google(audio,language='en-in')
       print(f"user said :{query}")

    except Exception as e:
       speak("say that again please...")
       return"none"
    return query

#time
def time():
    t= datetime.datetime.now().strftime("%H:%M:%S")
    speak("the running time is")
    speak(t)

# def date():
#     t1=datetime.datetime.now(tz=pytz.timezone('Asia'))
#     speak(t1.strtime('%d %B, of %Y'))

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
       speak("good morning")
    elif hour>12 and hour<18:
       speak("good afternoon")
    else:
       speak("good evening")
    speak("i am jarvis sir. please tell me how can help you")

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)   
    server.ehlo()
    server.starttls()
    server.login("kadamroshan5050@gmail.com","softwareengineer")
    server.sendemail("kadamroshan5050@gmail.com",to,content)
    server.close

def activate_jarvis():
    while True:
        query = Takecommand()
        if "jarvis open" in query:
            speak("I am ready, how can I help you?")
            main()
# For main function
if __name__ == "__main__":
    wish()
    while True:
    #if 1:

        query = Takecommand()

        if "open Notepad" in query:
            path1 = "C:\\Windows\\notepad.exe"
            os.startfile(path1)

        elif "close notepad " in query:
            speak("okay sir ,closing Notepad")
            os.system("taskkill/f /im notepad.exe")

        elif "time" in query:
            time()
        
        elif "Sarch Wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            speak(results)

        # elif "date" in query:
        #     date()
        
        elif "shut down the system" in query:
             os.system("shutdown /s /t 5")
                
        elif "restrat the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
             os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "open Microsoft edge" in query:
            path2 = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"
            os.startfile(path2)

        elif "open CMD" in query:
            path3 = "C:\\Windows\\system32\\cmd.exe"
            os.startfile(path3)

        elif "open control panel" in query:
            path4 = "C:\\Windows\\system32\\control.exe"
            os.startfile(path4)

        elif "open calculator" in query:
            path9 = "C:\\Program Files (x86)\\WindowsPowerShell\\Modules\Pester\\3.4.0\\Examples\\Calculator.exe"
            os.startfile(path9)    

        elif "open Word" in query:
            path5 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path5)
        elif "open PowerPoint" in query:
            path6 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path6)
        elif "open Excel" in query:
            path7 = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(path7)
            
        elif "open camera" in query:
          cap = cv2.VideoCapture(0)
          while True:
             ret, img = cap.read()
             cv2.imshow('webcam', img)
             k = cv2.waitKey(50)
             if k==27:
                 break;
          cap.release()
          cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "c:\\Users\\Aakash\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

    

        elif "Wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=5)
            speak("According to wikipedia")
            speak(results)
            #print(results)
        
        elif "play song on YouTube" in query:
            kit.playonyt("see you again")
        

        elif "open YouTube" in query:
            os.system("C:\\Users\\Aakash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")


        elif "open Facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open Instagram" in query:
            webbrowser.open("www.instagram.com")
        
        elif "open Google" in query:
            speak("sir,what should i serach on google")
            cm = Takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "Download" in query:
            from feature import DownloadYouTube
            DownloadYouTube()
        
        #To set on Alarm
        elif "set alarm" in query:
            speak("enter the time!")
            time= input(": enter the time : ")
            
            while True:
               Time_Ac = datetime.datetime.now()
               now = Time_Ac.strftime("%H:%M:%S")
            
               if now == time:
                speak("time to wake up sir!")
                playsound("D:\\project\\python gui\\Personal Assistant\\musin0\\trap-future-bass-royalty-free-music-167020.mp3")
                speak("Alarm closed!")
            
               elif now >time:
                 break;
        # send email
        elif "send email" in query:
         try:
            to = "akashkadam1889@gmail.com"
            speak("what should i send")
            content = Takecommand()
            sendEmail(to,content)
            speak("email send succesfully")
         except Exception as e:
             print(e)
            
        #whatsapp 
        elif "WhatsApp" in query:
          from whatsapp import sendMessage
          sendMessage()

        elif "no thanks" in query:
            speak("thanks for using me sir , have a good day")
            sys.exit()

        else :
            print("sorry")
            speak("sorry sir did not understood")

        #speak("sir,do you have any other task")
        def activate_jarvis():
         while True:
           query = Takecommand()
           if "jarvis open" in query:
            speak("I am ready, how can I help you?")

# Starting point
        if __name__ == "__main__":
          speak("I am listening for the wake word.")
          activate_jarvis()

