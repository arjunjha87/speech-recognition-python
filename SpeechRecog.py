import speech_recognition as sr
recog = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something:")
    audio = recog.listen(source)
    try:
        text = recog.recognize_google(audio)
        print("You said:")
        print(text)
    except:
        print("Sorry, couldn't recognize your speech.")
