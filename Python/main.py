#SmartSTT
#Importing the modules required for the program

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import light as li


listener = sr.Recognizer()                                       # Initialize the recognizer
engine = pyttsx3.init()                                          # Initialize the engine
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Used to speak to the user
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Used to take command from the user
def take_command():
    try:
        with sr.Microphone() as source:
            print('...')                                           #Tells Us that the assistant is ready to hear!
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:                                 #if we call alexa then only commands are accepted
                command = command.replace('alexa', '')
                #print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    # Analyzes the command
    if 'play' in command:                              #helps to play any song in youtube
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')         
        talk('Current time is ' + time)                #tells about the current time
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)                                    #tells about the details of any person/object that user wants
        talk(info)
                                           
     #some random rants                                      
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
        #driver call makes the assistant to blink the light
    elif 'driver' in command:
        li.root.after(10000, li.root.destroy)         #after 10 seconds the screen closes 
        li.root.mainloop()
        talk(command)
    
    #By saying thank you or stop the alexa stops running
    
    elif 'thank you' in command:
        exit()
    elif 'stop' in command:
        exit()
    else:
        talk('Please say the command again.')


while True:                     
    run_alexa()  
