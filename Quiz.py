import random
import pandas as pd
from fileread import ReadFile


def takeMainInput():
    exceldata = pd.read_excel(r'Words.xlsx')
    newfileobj = ReadFile(exceldata)
    quizansCapital = newfileobj.excel_file2()
    quizansCountry =newfileobj.excel_file()
    print(quizansCountry, quizansCapital)



takeMainInput()