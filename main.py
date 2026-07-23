#pip install speechrecognition
#            pyaudio
#            setuptools
#            pyttsx3

import speech_recognition as sr
import webbrowser
import pyttsx3
import music_lib
import winsound
from urllib.parse import quote_plus
import re
import random

# recognizer

r = sr.Recognizer()

r.energy_threshold = 300        
r.dynamic_energy_threshold = True
r.pause_threshold = 0.8           
r.phrase_threshold = 0.3
r.non_speaking_duration = 0.5


#text to speech

def speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    engine.setProperty("volume", 1.0)
    engine.setProperty("rate", 170)

    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# listening starting

mic = sr.Microphone()
print("Calibrating microphone... Please stay silent")

with mic as source:
    r.adjust_for_ambient_noise(source, duration=1)

print("Calibration complete.")

WAKE_WORDS = {
        "jarvis",
        "jarvis.",
        "jarvis?",
        "jaavis",
        "jarbis",
        "service"
}

def wake_word(text):
    words = re.findall(r"\b[a-z']+\b", text.lower())
    return any(word in WAKE_WORDS for word in words)


# websites

websites = {
    "google": "https://google.com",
    "youtube": "https://youtube.com",
    "wikipedia": "https://wikipedia.org",
    "chat gpt":  "https://chatgpt.com",
    "github": "https://github.com/Arpit-Singh-Chauhan",
    "instagram":  "https://www.instagram.com/arpit_singhchauhan1/",
    "linkedin":  "https://www.linkedin.com/in/arpit-singh-chauhan1209/",
}


# processing the command

def processCommand(c):
    c = c.lower().strip()

    parts = c.split(maxsplit=1)
    action = parts[0]
    arg = parts[1] if len(parts) > 1 else ""

    if action == "open":

        if arg in websites:
            speak(f"opening {arg}")
            webbrowser.open(websites[arg])
            return True
        
        else:
            speak("Sorry, I don't know that website.")
            return False

    elif action == "play":

        if arg in music_lib.music:
            speak(f"playing {arg}")
            webbrowser.open(music_lib.music[arg])
            return True

        elif any(word in arg for word in ["random", "song"]):
            speak("playing a random song for you")
            key = random.choice(list(music_lib.music))
            webbrowser.open(music_lib.music[key])
            return True

        elif "spotify" in arg:
            speak("opening spotify")
            webbrowser.open("https://open.spotify.com/playlist/78NDTpix9jThoMxdZ5eunP")
            return True

        else:
            speak("Sorry, I don't have that song.")
            return False


    elif action == "search":

        if arg:
            speak(f"searching {arg}")
            webbrowser.open(f"https://www.google.com/search?q={quote_plus(arg)}")
            return True

        else:
            speak("What would you like me to search for?")
            return False

    else:
        speak("Sorry, I don't know that command.")
        return False


#listening

def listen(timeout=2, phrase_time_limit=4):

    try:
        with mic as source:
            audio = r.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

            return r.recognize_google(audio, language="en-IN")

    except sr.UnknownValueError:
        return "UNKNOWN"

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        return None

    except sr.WaitTimeoutError:
        return "TIMEOUT"

    except Exception as e:
                print("Error:", e)
                return None


# exit

EXIT_WORDS = {
    "bye",
    "goodbye",
    "exit",
    "stop",
    "close yourself"
}

def exit_command(command):
    words = re.findall(r"\b[a-z']+\b", command.lower())
    return any(word in EXIT_WORDS for word in words)



RESPONSES = [
    "Yes Sir?",
    "I'm listening.",
    "How can I help?",
    "What can I do for you?"
]


if __name__ == "__main__":

    speak("Hii Sir")
    
    while True:

        print("Listening for wake word...")

        word = listen(timeout=None, phrase_time_limit=2)

        if word in ["UNKNOWN", "TIMEOUT", None]:
            continue

        print("Heard:", word)

        if wake_word(word):

            # winsound.Beep(1500, 200)

            speak(random.choice(RESPONSES))

            max_try = 3
            retries = 0

            while True:

                print("Listening for command...")

                command = listen(timeout=5, phrase_time_limit=6)

                if command == "TIMEOUT":
                    speak("No command received.")
                    break

                elif command == "UNKNOWN":
                    retries += 1

                    if retries == max_try:
                        speak("No command received, Going back to wake word")
                        break

                    speak("I didn't catch that, Please repeat the command")
                    continue

                if exit_command(command):
                    speak("Goodbye Sir.")
                    exit()          # full prog. close


                print("Command:", command)
                # processCommand(command)

                success = processCommand(command)
                if success:
                    break

                speak("Please say another command.")