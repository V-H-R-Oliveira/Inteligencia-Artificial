import csv, os
from AbstractBase import AbstractBase

class Atributos(AbstractBase):
    def __init__(self, filename):
        super().__init__(filename)
        self.__atributos: dict = {}
    
    def __repr__(self):
        return "Atributos: {}".format(self.__atributos)

    def getAtributos(self) -> dict:
        return self.__atributos 

    def readFile(self):
        PATH: str = os.getcwd() + "/data/{}".format(self.filename)
        with open(PATH, newline='') as csvfile:
            content: str = csv.reader(csvfile, delimiter=",")
            for index, row in enumerate(content):
                if index == 0:
                    continue
                elif len(self.__atributos) <= 0:
                    self.__atributos[index - 1] = tuple(row)
                else:
                    aux = {index-1:tuple(row)}
                    self.__atributos.update(aux)