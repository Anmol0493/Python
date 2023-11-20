import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Anmol")
    engine = pyttsx3.init(driverName='sapi5')

    while True:
        x = input("Enter what you want to speak: ")
        if x == "exit":
            engine.say("Thank you for using me.")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
