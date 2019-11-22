from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mHail: \x1b[0m"))

    if op == 0:
        hail = "Desconhecido"
    elif op == 1:
        hail = "Yes"
    elif op == 2:
        hail = "No"
    else: 
        raise AttributeError("Atributo inválido")    
    return hail

def hail() -> str:
    data: list = fetchData("hail")
    showData(data)
    hail: str = getUserInput()
    return hail