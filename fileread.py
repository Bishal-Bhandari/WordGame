import secrets

import pandas as pd


class ReadFile:
    def __init__(self,filedata):
        self.filedata = filedata

    def excel_file(self):
        colcountry = self.filedata['Country'].values
        randomvalue = secrets.choice(colcountry)
        return randomvalue
