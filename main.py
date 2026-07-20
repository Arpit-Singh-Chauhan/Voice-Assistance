#pip install speechrecognition
#            pyaudio
#            setuptools
#            pyttsx3

import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

websites = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "wikipedia": "https://wikipedia.org",
    "chat gpt":  "https://chatgpt.com",
    "github": "https://github.com/Arpit-Singh-Chauhan",
    "instagram":  "https://www.instagram.com/arpit_singhchauhan1/",
    "linkedin":  "https://www.linkedin.com/in/arpit-singh-chauhan1209/",
}

def processCommand(c):
    c = c.lower()

    if c.startswith("open "):
        website = c.split(maxsplit=1)[1]

        if website in websites:
            webbrowser.open(websites[website])
        else:
            speak("Sorry, I don't know that website.")

if __name__ == "__main__":
    print("Hey")
    speak("...Initializing jarvis...")
    while True:
        r = recognizer

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=1, phrase_time_limit=2)
            word = r.recognize_google(audio)
            # if "hello" in word.lower():
            if any(x in word.lower() for x in ["open", "pen", "ope"]):
                print("Wake word detected")
                speak("Yes")
                with sr.Microphone() as source:
                    print("Listening for command...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print(command)

                processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError:
            print("Speech Recognition service unavailable")

        except Exception as e:
            print(e)