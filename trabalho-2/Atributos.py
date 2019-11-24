import csv, os
from AbstractBase import AbstractBase
from Persistence import Persistence

class Atributos(AbstractBase):
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
                    data.append((index, row[0], row[1], row[2]))
        return data
    
    def persist(self):
        data: list = self.readFile()
        try:
            self.dbHandler.connect()
            self.dbHandler.insert("atributos", data)
            self.dbHandler.closeConnection()
        except Exception as e:
            raise e