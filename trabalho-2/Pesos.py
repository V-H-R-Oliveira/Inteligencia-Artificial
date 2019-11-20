import csv, os

class Pesos(object):
    def __init__(self, filename):
        self.__pesos = {}
        self.__filename = filename
    
    def __repr__(self):
        return "Pesos: {}".format(self.__pesos) 

    def getPeso(self) -> dict:
        return self.__pesos

    def setPesos(self, pesos: dict):
        self.__pesos = pesos
    
    def getFilepath(self) -> str:
        return self.__filename

    def setPesos(self, filename: str):
        self.__filename = filename
    
    def readFile(self):
        aux = {}
        PATH: str = os.getcwd() + "/{}".format(self.__filename)
        with open(PATH, newline='') as csvfile:
            content: str = csv.reader(csvfile, delimiter=",")
            for index, row in enumerate(content):
                if index == 0:
                    continue
                elif len(self.__pesos) <= 0:
                    self.__pesos[row[0]] = row[1]
                else:
                    aux = {row[0]:row[1]}
                    self.__pesos.update(aux)