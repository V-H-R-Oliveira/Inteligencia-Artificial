from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mLeaves: \x1b[0m"))

    if op == 0:
        leaves = "Desconhecido"
    elif op == 1:
        leaves = "Norm"
    elif op == 2:
        leaves = "Abnorm" 
    else: 
        raise AttributeError("Atributo inválido")    
    return leaves

def leaves() -> str:
    data: list = fetchData("leaves")
    showData(data)
    leaves: str = getUserInput()
    return leaves