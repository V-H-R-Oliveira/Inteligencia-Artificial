from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mLeaf malf: \x1b[0m"))

    if op == 0:
        leafMalf = "Desconhecido"
    elif op == 1:
        leafMalf = "Absent"
    elif op == 2:
        leafMalf = "Present" 
    else: 
        raise AttributeError("Atributo inválido")    
    return leafMalf

def leafMalf() -> str:
    data: list = fetchData("leaf_malf")
    showData(data)
    leafMalf: str = getUserInput()
    return leafMalf