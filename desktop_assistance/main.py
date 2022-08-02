from decimal import Context
#import pyttsx3
import smtplib
import wikipedia
import os
import datetime
#import speech_recognition as sr
import webbrowser
#import PyQt5
#from wikipedia.exceptions import WikipediaException
#import pyaudio

#pa = pyaudio.PyAudio()
#pa.get_default_input_device_info()

"""
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

# this function will speak according to current time


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('GOOD MORNING MASTER')

    elif hour >= 12 and hour < 18:
        speak('good afternoon master')

    else:
        speak('good evening')
    speak('I am your desktop assistant. Bryan. How may I help you?')

# this function will take command from the mic

"""
def takeCommand():
    pass
    #r = sr.Recognizer()
    # with sr.Microphone() as source:
    #   print("Listening.....")
    #  audio = r.listen(source)

    # try:
    #   print("Recognizing...")
    #  query = r.recognize_google(audio, language='en-us')
    # print(f"user said: {query}\n")
    # except Exception as e:
    #   print('say that again please')
    #  query = 'email to harry'
    query = input()
    return query.lower()


#speak("Initializing your desktop assistant")
#wishMe()
#query = takeCommand()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youemail@gmail.com', 'password')
    server.sendmail("harry@codewithharry.com", to, content)
    server.close()


def communicate(query):
    if 'wikipedia' in query.lower():
        #speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        return results
    
    elif 'youtube' in query.lower():
        url = 'youtube.com'
        webbrowser.open(url)
    
    elif 'google' in query.lower():
        url = 'google.com'
        webbrowser.open(url)
    
    elif 'stack overflow' in query.lower():
        url = 'stackoverflow.com'
        webbrowser.open(url)
    
    elif 'reddit' in query.lower():
        url = 'reddit.com'
        webbrowser.open(url)
    
    elif 'facebook' in query.lower():
        url = 'facebook.com'
        webbrowser.open(url)
    
    elif 'twitter' in query.lower():
        url = 'twitter.com'
        webbrowser.open(url)
    
    elif 'music' in query.lower():
        song_url = "C:\\Users\\Touching tap\\Music\\musics"
        songs = os.listdir(song_url)
        os.startfile(os.path.join(song_url, songs[0]))
    
    elif 'word' in query.lower():
        os.system('start files/Doc1.docx')
        
    elif 'ok' in query.lower():
        return "\n\nalright, what do you want me to do for you?"
    
    elif 'alright' in query.lower():
        return "\n\nokay, what can I do for you?"
    
    elif 'bye' in query.lower():
        return "\n\nalright boss, see you later"
        
    elif 'excel' in query.lower():
        os.system('start files/Doc1.csv')
        
    elif 'powerpoint' in query.lower():
        os.system('start files/Doc1.pptx')
    
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H.%M.%S")
        return f"MASTER, the time is {strTime}"
    
    elif 'food' in query:
        url = 'https://food.jumia.com.ng/'
        webbrowser.open(url)
        return "\n\nQuickly order online incase you can't cook"
    
    elif 'money' in query:
        url = 'https://mint.intuit.com/blog/how-to/ways-to-make-money-at-home/'
        webbrowser.open(url)
        return "\n\nlet me show you a few ways to make money"
    
    elif 'email to' in query:
        try:
            return "\n\nWhat should I send?"
            content = query
            return "\n\nto"
            to = query
            sendEmail(to, content)
            return '\n\nemail has been sent successfully'
    
        except Exception as e:
            return "\n\nthere was a minor problem"
    
    else:
        return "\n\nok, what do you think I can do for you?"
