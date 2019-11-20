from Pesos import Pesos
from Atributos import Atributos
from Casos import Casos

if __name__ == "__main__":
    pesos: Pesos = Pesos("pesos.csv")
    atributos: Atributos = Atributos("atributos.csv")
    casos: Casos = Casos("casos.csv")
    pesos.readFile()
    atributos.readFile()
    casos.readFile()

    print(pesos, atributos, casos, sep="\n\n")