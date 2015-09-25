import random, time, sys

list = ["Maybe someday.", "Nothing.", "Follow the seahorse.",
        "I don't think so.", "No.", "Yes.", "Try Asking Again."]

def main():
    print("Welcome to the Magic Conch Shell")
    print("Enter your yes or no question: ")

    question = raw_input("> ")

    print("\nPulling String\n")
    time.sleep(5)
    print(random.choice(list))
    print("")
    print("THE SHELL KNOWS ALL!")
    time.sleep(3)
    askAgain()

def askAgain():
    print("Would you like to ask another question? y/n")
    again = raw_input("> ")
    if again == "y":
        main()
    elif again == "n":
        print("Goodbye")
        time.sleep(1.5)
        sys.exit(0)
    else:
        print("Please put a y for yes and an n for no.")
        askAgain()
main()


