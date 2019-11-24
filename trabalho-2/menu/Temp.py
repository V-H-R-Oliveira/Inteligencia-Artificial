from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mTemp: \x1b[0m"))

    if op == 0:
        temp = "Desconhecido"
    elif op == 1:
        temp = "lt_norm"
    elif op == 2:
        temp = "norm"
    elif op == 3:
        temp = "gt_norm" 
    else: 
        raise AttributeError("Atributo inválido")    
    return temp

def temp() -> str:
    data: list = fetchData("temp")
    showData(data)
    temp: str = getUserInput()
    return temp