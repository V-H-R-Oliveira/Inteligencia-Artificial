from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mSeed Size: \x1b[0m"))

    if op == 0:
        seedSize = "Desconhecido"
    elif op == 1:
        seedSize = "Norm"
    elif op == 2:
        seedSize = "lt_norm"
    else: 
        raise AttributeError("Atributo inválido")    
    return seedSize

def seedSize() -> str:
    data: list = fetchData("seed_size")
    showData(data)
    seedSize: str = getUserInput()
    return seedSize