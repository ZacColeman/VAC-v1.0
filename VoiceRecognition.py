import speech_recognition as sr
import pyttsx3 as p

def speechToText():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        text = r.listen(source)

        try:
            recognized_text = r.recognize_google(text)
            return recognized_text
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as e:
            print("")


def textToSpeech(response):
    engine = p.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    engine.say(response)
    engine.runAndWait()


