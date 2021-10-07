#importing python modules
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os
import chime

#setting up the assistant voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#function for extrracting email and password from local file
def emailExtract():
    path = 'C:\\' #input your file location here where you have kept the email and password
    with open(f'{path}\\email.txt','r') as f:
        email = f.read()
    with open(f'{path}\\password.txt','r') as f:
        password = f.read()

    return email,password


#function for speaking
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#Wishing Function using speak Function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Sir!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon Sir!')
    else:
        speak('Good Evening Sir!')

    speak('My name is Sara. And i am your assistant. Please tell me how may i help you')


#function for taking the commands
def takeCommand():
    #it takes microphone input from the user and give string as output
    r = sr.Recognizer()
    with sr.Microphone() as source:

        #sound for listening indicator
        chime.info()
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak('recognising your query sir')
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #this section is for whenever any 
        print(e)
        print('Say that again please...')
        return "None"
    return query


def sendEmail(to, content):
    email,password  = emailExtract()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(email,password)
    server.sendmail(email,to,content)
    server.close()


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        #logics for tasks execution
        if 'wikipedia' in query:
            speak('Searching wikipedia for your answer sir...')
            query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences = 2)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open google' in query:
            webbrowser.open('google.com') 

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        
        #for playing music from local directory
        elif 'play music' in query:
            music_dir = ''  #enter the music file location here
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, right now the the is {strTime}')

        elif 'open whatsapp' in query:
            whatsappPath = ''   #enter application ap location here
             
            os.startfile(whatsappPath)

        elif 'email to friend' in query:
            try:
                speak('Sir, Give me the instructions for the email!')
                content = takeCommand()
                to = ''  #input here the email to which you wan to send email
                sendEmail(to, content)
                speak('Sir, The email has been sent to your friend')
            except Exception as e:
                print(e)
                speak('Sorry Sir! i am not able to send this email at the moment. Please try after some time.')
        
        #for exiting the assistant
        elif 'shutdown assistant' in query:
            speak('I am shutting down sir. Please call me whenever you need any assistance. Thank you!')
            exit()


            #you can further increase it's functinality as per your ideas