from importlib import reload

print("\n===>>WELCOME to our game word and quiz.<<===")


def gamechoice():
    opt = True
    while opt:
        if opt:
            choice = input("\nPlease press 'a' or 1 for Word Guess Game and press 'b' or 2 for Quiz. Also, 'c' or 3 to "
                           "exit: ")
            if choice == "a" or choice == "A" or choice == str(1):
                # importing guess word file
                if 'Guessword' in dir():  # if it has already been imported
                    reload(Guessword)
                else:
                    import Guessword
            elif choice == "b" or choice == "B" or choice == str(2):
                # importing quiz file
                if 'Quiz' in dir():  # if it has already been imported
                    reload(Quiz)
                else:
                    import Quiz
            elif choice == "c" or choice == "C" or choice == str(3):
                print("Thank you for playing.")
                break
            else:
                print("Please choose from given option only.")
        else:
            print("Thank you for playing.")
            break


gamechoice()
