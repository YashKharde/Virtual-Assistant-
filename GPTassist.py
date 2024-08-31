import pyttsx3
import speech_recognition as sr

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Audio captured, processing...")
        try:
            data = recognizer.recognize_google(audio)
            print("You said:", data)
            return data
        except sr.UnknownValueError:
            engineReply = pyttsx3.init()
            engineReply.say("Google Speech Recognition could not understand audio")
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            engineReply.say("Could not request results from Google Speech Recognition")
            print(f"Could not request results from Google Speech Recognition; {e}")

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Main function to listen and speak
if __name__ == "__main__":
    text = sptext()
    if text:
        speak_text(f"You said: {text}")


#Run command //-- python f:/Python_Proj/GPTassist.py --//