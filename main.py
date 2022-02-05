print("===>>WELCOME to our game word and quiz.<<===")
choice_word = input("Please press 'a' or 1 for Word Guess Game and press 'b' or 2 for Quiz: ")

def gamechoice(choice):
    if choice == "a" or choice == "A" or choice == str(1):
        import Guessword
    elif choice == "b" or choice == "B" or choice == str(2):
        print("On the way")
    elif choice == "c" or choice == "c" or choice == str(3):
        print("break")
    else:
        print("Please choose from given option only.")


gamechoice(choice_word)