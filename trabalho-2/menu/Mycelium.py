from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mMycelium: \x1b[0m"))

    if op == 0:
        mycelium = "Desconhecido"
    elif op == 1:
        mycelium = "Absent"
    elif op == 2:
        mycelium = "Present" 
    else: 
        raise AttributeError("Atributo inválido")    
    return mycelium

def mycelium() -> str:
    data: list = fetchData("mycelium")
    showData(data)
    mycelium: str = getUserInput()
    return mycelium