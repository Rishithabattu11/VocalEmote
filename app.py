import speech_recognition as sr
from transformers import pipeline

recognizer = sr.Recognizer()
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")
def recognize_speech():
    with sr.Microphone() as source:
        print("Please speak now...")
        recognizer.adjust_for_ambient_noise(source, duration=1) 
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=15)  
        print("Audio captured.")
        try:
            text = recognizer.recognize_google(audio)
            print("You said: ", text)
            emotion = emotion_classifier(text)
            print(f"Detected emotion: {emotion[0]['label']}")
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Request failed; check your internet connection.")
if __name__ == "__main__":
    recognize_speech()
