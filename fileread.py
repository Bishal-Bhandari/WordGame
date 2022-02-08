import secrets


class ReadFile:
    def __init__(self, filedata):
        self.filedata = filedata

    def excel_file(self):
        colcountry = self.filedata['Country'].values
        return colcountry

    def excel_file2(self):
        colcapital = self.filedata['Capital'].values
        return colcapital
