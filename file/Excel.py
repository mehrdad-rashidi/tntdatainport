import pandas as pd


class Excel:
    __path = None
    __sheetName = None
    __excel_file = None

    def __init__(self, path):
        try:
            self.path = path
            self.excel_file = pd.ExcelFile(self.path)

        except FileNotFoundError:
            print('File not fount in path : ', self.path)

    def read_sheet(self, sheet_name):
        excel_data_frame = self.excel_file.parse(sheet_name=sheet_name)
        return excel_data_frame

    @property
    def sheet_name(self) -> list:
        self.__sheetName = self.excel_file.sheet_names
        return self.__sheetName

    @property
    def path(self):
        return self.__path

    @sheet_name.setter
    def sheet_name(self, sheet_name):
        self.__sheetName = sheet_name

    @path.setter
    def path(self, path):
        self.__path = path
