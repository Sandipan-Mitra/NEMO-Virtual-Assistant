from Face.Ear import listen
from Face.Mouth import speak
from GreetMe import greet
from Main_Nemo import MainExecution

def wakeup_detected():
    print("Say \"wake up\" to start. or \"shutdown\" to quit.")
    command = listen()

    if "wake up" in command:
        speak(f"{greet()} I'm Nemo, your virtual assistant. I'm ready to assist you.")
        MainExecution()
    elif "shutdown" in command:
        # speak("Goodbye.\n\t See you soon.")
        speak(" It's been a long day without you, my friend.\n\tAnd I'll tell you all about it when I see you again.\n\tWhen I see you again...\n\tGoodbye.")
        exit()

    else:
        pass