import pandas as pd
from fileread import ReadFile
import pyttsx3
userscore = 0
totalquestion = 0


def takeMainInput():
    global userscore
    global totalquestion
    exceldata = pd.read_excel(r'Words.xlsx')  # read file
    newfileobj = ReadFile(exceldata)  # create onj
    quizansCapital = newfileobj.excel_file2()  # read capital column
    quizansCountry = newfileobj.excel_file()  # read country column
    lencountry = len(quizansCountry)
    for x in range(lencountry):
        totalquestion += 1  # count num of question
        quizansCapital[x] = quizansCapital[x].upper()
        useransCapital = str(
            input("(" + str(totalquestion) + "). What is the capital of " + str(quizansCountry[x]).upper() + ": ")).upper()  # user ans
        if useransCapital == str(quizansCapital[x]):
            userscore += 1
            print("Proceeding to the next question....\n")
        else:
            userscore += 0
            print("Proceeding to the next question....\n")

    print("Your score is " + str(userscore) + "\\" + str(totalquestion) + ".")
    pyttsx3.speak("Your score is " + str(userscore) + ".")
    userchoice = input("\nPress \"Y\" to play again and \"N\" to exit to main menu: ").upper()
    if userchoice == "Y":
        takeMainInput()
    else:
        import main


takeMainInput()
