from Pesos import Pesos

if __name__ == "__main__":
    pesos: Pesos = Pesos("pesos.csv")
    pesos.readFile()
    print(pesos)