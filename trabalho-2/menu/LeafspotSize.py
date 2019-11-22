from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mLeafspot size: \x1b[0m"))

    if op == 0:
        leafspotSize = "Desconhecido"
    elif op == 1:
        leafspotSize = "lt_1/8"
    elif op == 2:
        leafspotSize = "gt_1/8"
    elif op == 3:
        leafspotSize = "dna"    
    else: 
        raise AttributeError("Atributo inválido")    
    return leafspotSize

def leafspotSize() -> str:
    data: list = fetchData("leafspot_size")
    showData(data)
    leafspotSize: str = getUserInput()
    return leafspotSize