import csv, os
from AbstractBase import AbstractBase

class Atributos(AbstractBase):
    def __init__(self, filename):
        super().__init__(filename)
        self.__atributos: dict = {}
    
    def __repr__(self):
        return "Atributo: {}".format(self.__atributos) 

    def readFile(self):
        aux = tuple()
        PATH: str = os.getcwd() + "/{}".format(self.filename)
        with open(PATH, newline='') as csvfile:
            content: str = csv.reader(csvfile, delimiter=",")
            for index, row in enumerate(content):
                if index == 0:
                    continue
                elif len(self.__atributos) <= 0:
                    self.__atributos[index - 1] = (row[0], row[1], row[2])
                else:
                    aux = {index-1:(row[0], row[1], row[2])}
                    self.__atributos.update(aux)
        
        print(self.__atributos)