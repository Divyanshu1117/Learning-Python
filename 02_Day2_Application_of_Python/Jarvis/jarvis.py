# pip install pyaudio pyttsx3 SpeechRecognition wikipedia

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Initialize pyttsx3
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # [0]=Male, [1]=Female (check once)


def speak(audio):
    print(f"Jarvis: {audio}")
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    """It takes microphone input from the user and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300  # avoid background noise
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Could not understand audio, please say that again...")
        return "None"
    except sr.RequestError:
        print("Could not request results, check your internet connection")
        return "None"

    return query


def sendEmail(to, content):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_app_password")
        server.sendmail("your_email@gmail.com", to, content)
        server.close()
        return True
    except Exception as e:
        print("Email error:", e)
        return False


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()
            if query:
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
                except Exception as e:
                    speak("Sorry, I could not fetch details from Wikipedia.")
                    print("Wiki error:", e)
            else:
                speak("Please tell me what to search on Wikipedia.")

        elif "open youtube" in query:
            webbrowser.open("https://youtube.com")

        elif "open google" in query:
            webbrowser.open("https://google.com")

        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com")

        elif "play bhajan" in query:
            music_dir = "D:\\BHAJAN"
            if os.path.exists(music_dir):
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found in the Bhajan folder.")
            else:
                speak("Bhajan folder not found.")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif "open code" in query:
            codePath = (
                r"C:\Users\vashi\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            )
            if os.path.exists(codePath):
                os.startfile(codePath)
            else:
                speak("VS Code path is not correct on this system.")

        elif "email to divyanshu" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "divyanshu18@gmail.com"
                if sendEmail(to, content):
                    speak("Email has been sent!")
                else:
                    speak("Sorry, I could not send the email.")
            except Exception as e:
                print(e)
                speak(
                    "Sorry my friend Divyanshu bhai, I am not able to send this email"
                )

        elif "quit" in query or "exit" in query:
            speak("Goodbye Sir, have a great day!")
            break

        else:
            print("No query matched")