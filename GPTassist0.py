import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time  

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  # -------- Listening
        speak_text("Listening...")
        time.sleep(0.5)  # -------------- for Printing before Recording
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Audio captured, processing...")
        try:
            data = recognizer.recognize_google(audio)
            print("You said:", data)
            return data.lower()  #-------- Lower case
        except sr.UnknownValueError:
            engineReply = pyttsx3.init()
            engineReply.say("Google Speech Recognition could not understand audio")
            engineReply.runAndWait()
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            engineReply.say("Could not request results from Google Speech Recognition")
            engineReply.runAndWait()
            print(f"Could not request results from Google Speech Recognition; {e}")

def speak_text(text):
    engine = pyttsx3.init()
    # Set properties for the voice (slower speed)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # Reduce the rate by 50
    engine.say(text)
    engine.runAndWait()

def handle_task(task):
    if "open youtube" in task:
        speak_text("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "tell me a joke" in task:
        joke = pyjokes.get_joke()
        print(joke)
        speak_text(joke)
    elif "date" in task or "time" in task:
        now = datetime.datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        speak_text(f"The current date and time is {date_time}")
    elif "what is your name" in task or "who created you" in task:
        print("I am Jarvis, and Sir Yash Kharde made me.")
        speak_text("I am Jarvis, and Sir Yash Kharde made me.")
    elif "exit" in task:
        speak_text("Going to main menu")
        return False
    else:
        speak_text("I did not understand that. Please try again.")
    return True

def main():
    while True:
        text = sptext()
        if text:
            if "exit" in text:
                speak_text("See You SOON?")
                break  # ------------------------------- Exit For exit
            elif "hey jarvis" in text:
                speak_text("What can I do for you today?")
                while True:
                    task = sptext()  # Listen for the task after the initial greeting
                    if task and not handle_task(task):
                        break  # ----------------------- if user said exit
            else:
                speak_text("For using me, try speaking 'Heyy Jarvis' or say 'exit' to quit.")
                
        # Small delay to avoid continuous loop if no input is detected
        print("Listening again...")

#main
if __name__ == "__main__":
    main()

# ---------------------------------- f:/Python_Proj/GPTassist0.py