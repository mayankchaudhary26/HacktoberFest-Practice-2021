#install the google translator library from the Command Prompt=>
#pip install googletrans
#pip install SpeechRecognition
#pip install PyAudio (facing problem may need cracked version)
#pip install gTTS 
import googletrans
from googletrans.client import Translator
import speech_recognition as sr
import gtts
import playsound

recognizer=sr.Recognizer()

#prints the list of all languages accessible by Google Translator
print(googletrans.LANGUAGES)

#making the tranlator
translator=googletrans.Translator()

print("List of all languages accessed by Google Translater")
required_language=input("Enter your choosen language code in which you want to translate:")

try:
    with sr.Microphone() as source:
        print("Speak Now........")
        voice=recognizer.listen(source)
        text=recognizer.recognize_google(voice)
        print(text)
except:
    pass

#create the translated text
translated=translator.translate(text,dest=required_language)
print(translated.text)
#we might get error 
#install the alpha version of the package from Command Prompt=>
#pip install googletrans==3.1.0a0

#convert the translated text to audio file
required_audio=gtts.gTTS(translated.text,lang=required_language)
required_audio.save("Converted Audio.mp3")

#playing the converted audio file 
playsound.playsound("Converted Audio.mp3")
