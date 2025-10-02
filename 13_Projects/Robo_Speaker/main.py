import pyttsx3

if __name__ == "__main__":
    print("Welcome to Robo_Speaker 1.1 Created by Aashish...")
    engine = pyttsx3.init()

    while True:
        comm = input("Enter what do you want me to pronounce (or 'q' to quit): ")
        if comm.lower() == 'q':
            print("Exiting Robo_Speaker!")
            engine.say("Bye Bye.. Meet you next time!")
            engine.runAndWait()
            break
        engine.say(comm)
        engine.runAndWait()