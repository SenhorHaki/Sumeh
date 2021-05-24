#Arquivo principal.
import speech_recognition as sr

#cria um reconhecedor
r = sr.Recognizer()

#Abrindo o microfone para captura
with sr.Microphone() as source:
    audio = r.listen(source)

    print(r.recognize_google(audio))