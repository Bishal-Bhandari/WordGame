import random
import pandas as pd
from fileread import ReadFile
import secrets

full_word = ''
scorecount = 0
questioncount = 0

def take_input():
    x = 0
    try:
        exceldata = pd.read_excel(r'Words.xlsx')
        wordobj = ReadFile(exceldata)
        global full_word  # for original word so global var
        fullwordran = secrets.choice(wordobj.excel_file())  # for word after using random fun
        full_word = fullwordran.upper()
    except ValueError:
        print("Error in File.")
    length_true = len(full_word)
    lengths = int(length_true / 2)
    guessnumber = str(lengths)
    full_list = list(full_word)
    while x < lengths:
        full_list = random.sample(full_list, length_true)
        full_list = ''.join(full_list)
        x += 1
    print("Word is: " + full_list + ".\nYou have " + guessnumber + " guesses in total.")
    return [lengths, full_word]


def check_words():
    list_data = take_input()
    guess_word = ""
    counter = 0
    limit_off = False
    while list_data[1] != guess_word and not limit_off:
        if counter < list_data[0]:
            guess_word = input(f"\nThis is chance " + str(counter + 1) + ". Enter a guess word: ").upper()
            counter += 1
        else:
            limit_off = True
    return limit_off


def result():
    result_data = check_words()
    userinput = True
    global scorecount
    global questioncount
    while userinput:
        questioncount += 1
        if result_data:
            scorecount += 0
            print("You LOSE!!! Better luck next time.")
            print("Correct answer is: " + full_word)
            print("You have " + str(scorecount) + "/" + str(questioncount) + " answer correct.")
            userchoice = input("\nPress \" Y \" to play again and \"N\" to go to the menu: ").upper()
            if userchoice == "Y":
                result()
            else:
                userinput = False
                break
        else:
            scorecount += 1
            print("You win!!! CONGRATULATION.")
            print("You have " + str(scorecount) + "/" + str(questioncount) + " answer correct.")
            userchoice = input("\nPress \" Y \" to play again and \"N\" to go to the menu: ").upper()
            if userchoice == "Y":
                result()
            else:
                userinput = False
                break


result()
