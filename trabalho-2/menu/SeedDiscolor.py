from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mSeed Discolor: \x1b[0m"))

    if op == 0:
        seedDiscolor = "Desconhecido"
    elif op == 1:
        seedDiscolor = "Absent"
    elif op == 2:
        seedDiscolor = "Present"
    else: 
        raise AttributeError("Atributo inválido")    
    return seedDiscolor

def seedDiscolor() -> str:
    data: list = fetchData("seed_discolor")
    showData(data)
    seedDiscolor: str = getUserInput()
    return seedDiscolor