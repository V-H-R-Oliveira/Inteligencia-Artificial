from Pesos import Pesos
from Atributos import Atributos

if __name__ == "__main__":
    pesos: Pesos = Pesos("pesos.csv")
    atributos: Atributos = Atributos("atributos.csv")
    # pesos.readFile()
    atributos.readFile()