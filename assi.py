

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser as wb

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...........')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'eva' in command:
                command = command.replace('eva', '')
                print(command)

    except Exception as ex:

        return "None"
    return command


def run_eva():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("current time is " + time)
    elif 'who is the ' in command:
        person = command.replace('who is the','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'yourself' in command:
        talk(' myself eva i am a personal voice assistant designed by students of Vishwakarma institute of information technology')
    elif ' welcome everyone' in command:
        talk(' Hello everyone    glad to see you all   hope youb all are fine  Take care of yourself and your family   stay safe ')
    elif 'siri' in command:
        talk('dont take her name infront of me')
    elif 'single' in command:
        talk(' no i am in serious relationship with wifi')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif 'good morning' in command:
        talk('good morning sir')
    elif 'good afternoon' in command:
        talk('good afternoon sir')
    elif 'how are you' in command:
        talk('i am fine sir ')
    elif 'whatsapp' in command:
        talk('opening whatsapp')
        wb.open("web.whatsapp.com")
    elif 'instagram' in command:
        talk('opening instagram')
        wb.open("web.instagram.com")
    elif 'hello' in command:
        talk('hello sir how can i help you')
    else:
        talk("sorry i didnt get that please say it again")



while True:
    run_eva()
