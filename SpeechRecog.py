import speech_recognition as sr
recog = sr.Recognizer()
with sr.Microphone() as source:
    audio = recog.listen(source)
    try:
        text = recog.recognize_google(audio)
        print(text)
    except:
        print("Connectivity problem.")