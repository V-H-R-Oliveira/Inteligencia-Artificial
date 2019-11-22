from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mInt discolor: \x1b[0m"))

    if op == 0:
        intDiscolor = "Desconhecido"
    elif op == 1:
        intDiscolor = "None"
    elif op == 2:
        intDiscolor = "Brown"
    elif op == 3:
        intDiscolor = "Black"
    else: 
        raise AttributeError("Atributo inválido")    
    return intDiscolor

def intDiscolor() -> str:
    data: list = fetchData("int_discolor")
    showData(data)
    intDiscolor: str = getUserInput()
    return intDiscolor