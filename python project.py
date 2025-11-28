import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
engine= pyttsx3.init()
engine.setProperty(' rate', 175) 
engine.setProperty(' volume', 1.0) 
def speak(text):
    "Speak the given text."
    engine.say(text)
    engine.runAndWait()
def greet_user():
    "Greet the user based on the time."
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you today?")
def take_command():
    "Listen to the user and return the command as text."
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio=recognizer.listen(source)
    try:
        print("Recognizing...")
        command=recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {command}\n")
    except Exception:
        print("Sorry, I didn't catch that. Please say it again.")
        return ""
    return command.lower()
def main():
    greet_user()
    while True:
        command= take_command()
        if 'time' in command:
            current_time= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}")
        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif 'play music' in command:
            speak("Playing music from your computer")
            music_dir = "C:\\Users\\Public\\Music"  
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye! Have a nice day.")
            break
        elif command != " ":
            speak("Sorry, I didn’t understand that command.")
if __name__ == "__main__":
    main()
