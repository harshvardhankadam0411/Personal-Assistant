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


# Initialize speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 200)

# Function to speak audio
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Function to convert voice to text
def Takecommand(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=50, phrase_time_limit=1)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        speak("Say that again, please...")
        return "none"
    return query.lower()

# Function to get the current time
def time_now():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

# Function to wish the user
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Jarvis, sir. Please tell me how can I assist you")

# Function to send an email
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("your_email@gmail.com", "your_password")
    server.sendmail("your_email@gmail.com", to, content)
    server.close()

# Function to get time
def time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")

# Function to send an email
def sendEmail(to, content):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("your_email@gmail.com", "your_password")
        server.sendmail("your_email@gmail.com", to, content)
        server.close()
        speak("Email sent successfully!")
    except Exception as e:
        speak("Sorry, I couldn't send the email. Please check the email address and try again.")

# Function to fetch weather
def getWeather(city):
    api_key = 'your_openweathermap_api_key'
    base_url = f'http://api.openweathermap.lkjorg/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(base_url)
    data = response.json()
    if data["cod"] != "404":
        main = data['main']
        temperature = main['temp']
        weather_description = data['weather'][0]['description']
        speak(f"The temperature in {city} is {temperature - 273.15}°C with {weather_description}")
    else:
        speak("City not found")



# Main function
def main():
    wish()
    while True:
        query = Takecommand()

        if "open notepad" in query:
            path = "C:\\Windows\\notepad.exe"
            os.startfile(path)

        elif "close notepad" in query:
            speak("Okay sir, closing Notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "time" in query:
            time_now()

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "open microsoft edge" in query:
            path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"
            os.startfile(path)

        elif "open cmd" in query:
            os.startfile("C:\\Windows\\system32\\cmd.exe")

        elif "open control panel" in query:
            os.startfile("C:\\Windows\\system32\\control.exe")

        elif "open calculator" in query:
            os.startfile("calc.exe")

        elif "open word" in query:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path)

        elif "open powerpoint" in query:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path)

        elif "open excel" in query:
            path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(path)

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("Webcam", img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "play music" in query:
            music_dir = "C:\\Users\\Aakash\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak(f"According to Wikipedia, {results}")

        elif "play song on youtube" in query:
            kit.playonyt("See You Again")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            cm = Takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "set alarm" in query:
            speak("Please enter the time!")
            alarm_time = input(": Enter the time (HH:MM:SS): ")
            while True:
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                if current_time == alarm_time:
                    speak("Time to wake up, sir!")
                    playsound("D:\\project\\python gui\\Personal Assistant\\musin0\\trap-future-bass-royalty-free-music-167020.mp3")
                    break

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = Takecommand()
                to = "ds5864065@gmail.com"
                sendEmail(to, content)
                speak("Email sent successfully!")
            except Exception as e:
                print(e)
                speak("Sorry, I am unable to send the email.")

        elif "no thanks" in query:
            speak("Thanks for using me, sir. Have a great day!")
            sys.exit()


# Run the main function
if __name__ == "__main__":
     speak("I am listening for the wake word.")
     main()
