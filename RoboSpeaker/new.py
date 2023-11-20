import win32com.client as wincom

speaker = wincom.Dispatch("SAPI.SpVoice")

print("Welcome to RoboSpeaker 1.1. Created by Anmol")

while True:
    x = input("Enter what you want to speak: ")
    if x == "exit":
        speaker.Speak("Thank you for using me.")
        break
    speaker.Speak(x)