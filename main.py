import random
import pandas as pd
from fileread import ReadFile


def take_input():
    x = 0
    try:
        exceldata = pd.read_excel(r'Words.xlsx')
        wordObj = ReadFile(exceldata)
        full_word = wordObj.excel_file()
        # full_word = input("Enter a word: ")
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
    print("Word is: " + full_list + " and you have " + guessnumber + " guesses.")
    return [lengths, full_word]


def check_words():
    list_data = take_input()
    guess_word = ""
    counter = 0
    limit_off = False
    while list_data[1] != guess_word and not limit_off:
        if counter < list_data[0]:
            guess_word = input(f"This is chance " + str(counter+1) + ". Enter a guess word: ")
            counter += 1
        else:
            limit_off = True
    return limit_off


def result():
    result_data = check_words()
    if result_data:
        print("You Lose!!! Better luck next time.")
    else:
        print("You win!!! Congratulation.")


result()
