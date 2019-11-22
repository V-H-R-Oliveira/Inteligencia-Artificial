from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mPrecip: \x1b[0m"))

    if op == 0:
        precip = "Desconhecido"
    elif op == 1:
        precip = "lt_normal"
    elif op == 2:
        precip = "Normal"
    elif op == 3:
        precip = "gt_normal" 
    else: 
        raise AttributeError("Atributo inválido")    
    return precip

def precip() -> str:
    data: list = fetchData("precip")
    showData(data)
    precip: str = getUserInput()
    return precip