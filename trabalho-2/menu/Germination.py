from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mGermination: \x1b[0m"))

    if op == 0:
        germination = "Desconhecido"
    elif op == 1:
        germination = "90_100%"
    elif op == 2:
        germination = "80_89%"
    elif op == 3:
        germination = "lt_80%"
    else: 
        raise AttributeError("Atributo inválido")    
    return germination

def germination() -> str:
    data: list = fetchData("germination")
    showData(data)
    germination: str = getUserInput()
    return germination