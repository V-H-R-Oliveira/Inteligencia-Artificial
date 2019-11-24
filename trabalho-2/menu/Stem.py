from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mStem: \x1b[0m"))

    if op == 0:
        stem = "Desconhecido"
    elif op == 1:
        stem = "Norm"
    elif op == 2:
        stem = "Abnorm"
    else: 
        raise AttributeError("Atributo inválido")    
    return stem

def stem() -> str:
    data: list = fetchData("stem")
    showData(data)
    stem: str = getUserInput()
    return stem