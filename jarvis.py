import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine=pyttsx3.init('sapi5') #To take voices.
voices=engine.getProperty('voices')
 #voices[0].id will give a male's voice(named David).While voices[1] will give a female's voice(named Hazel).add()

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour=int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis! Please tell me How may I help you!")  

def takeCommand(): 
#This function will take micropjone input from the user and returns string output.
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        #To check if error occurs.
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print('say that again pls ')
        return "None" #It will return a none string if any problem occurs.
    return query  

if __name__=='__main__':
    WishMe()
    while True:
        query=takeCommand().lower()

        #Logic for executing tasks on query.
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.org")
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query:
            codepath="C:\\Users\\Anzeeta Giri\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            #single slashes in the path is coverted into double slashes to escape the slash character.To escape
            # / in python we use '/' before /.  
            os.startfile(codepath)
            

     
