command = ""
started = False
stopped = False

while True:
    command = input("Please enter the command: ").lower()   # use help lower to avoid using it everywhere
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            print("Starting car...")
    elif command == "stop":
        if stopped:
            print("Car has already stopped")
        else:
            stopped = True
            print("Car is stopping....")
    elif command == "help":
        print("""
start - starting the car
stop - stopping the car
quit - quitting the game 
                """)
    elif command == "quit":
        break
    else:
        print("I don't understand what you are typing.")