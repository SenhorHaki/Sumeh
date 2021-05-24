#Arquivo principal.

import speech_recognition as sr

#cria um reconhecedor
r = sr.Recognizer()

#Abrindo o microfone para captura
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) #Definindo microfone como fonte de audio

    
        print(r.recognize_google(audio, language='pt'))
