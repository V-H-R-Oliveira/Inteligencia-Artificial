import csv, os
from AbstractBase import AbstractBase
from Persistence import Persistence

class Casos(AbstractBase):
    def __init__(self, filename: str):
        super().__init__(filename)
    
    def readFile(self) -> list:
        data: list = []
        PATH: str = os.getcwd() + "/data/{}".format(self.filename)
        with open(PATH, newline='') as csvfile:
            content: str = csv.reader(csvfile, delimiter=",")
            for index, row in enumerate(content):
                if index == 0:
                    continue
                else:
                    data.append(tuple(row))
        return data    

    def persist(self):
        data: list = self.readFile()
        try:
            self.dbHandler.connect()
            self.dbHandler.insert("casos", data)
            self.dbHandler.closeConnection()
        except Exception as error:
            raise error