from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mFruiting Bodies: \x1b[0m"))

    if op == 0:
        fruitingBodies = "Desconhecido"
    elif op == 1:
        fruitingBodies = "Absent"
    elif op == 2:
        fruitingBodies = "Present"
    else: 
        raise AttributeError("Atributo inválido")    
    return fruitingBodies

def fruitingBodies() -> str:
    data: list = fetchData("fruiting_bodies")
    showData(data)
    fruitingBodies: str = getUserInput()
    return fruitingBodies