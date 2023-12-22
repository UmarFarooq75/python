import pyttsx3

def robospeaker():
    engine = pyttsx3.init()
    while True:
        x = input("Enter What You Want Me to Speak or Enter 'e' for Exit: ")
        if x.lower() == "e":
            speak(engine, "bye bye friend")
            break
        else:
            speak(engine, x)

def speak(engine, message):
    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    print("            Welcome to Robo-Speaker Program")
    robospeaker()
