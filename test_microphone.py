import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Please speak now...")
    recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
    audio = recognizer.listen(source)
    print("Audio captured.")

    try:
        print("You said: ", recognizer.recognize_google(audio))
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Request failed; check your internet connection.")
