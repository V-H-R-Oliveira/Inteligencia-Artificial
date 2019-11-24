from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mSeed: \x1b[0m"))

    if op == 0:
        seed = "Desconhecido"
    elif op == 1:
        seed = "Norm"
    elif op == 2:
        seed = "Abnorm"
    else: 
        raise AttributeError("Atributo inválido")    
    return seed

def seed() -> str:
    data: list = fetchData("seed")
    showData(data)
    seed: str = getUserInput()
    return seed