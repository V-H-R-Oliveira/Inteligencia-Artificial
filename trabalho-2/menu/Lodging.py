from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mLodging: \x1b[0m"))

    if op == 0:
        lodging = "Desconhecido"
    elif op == 1:
        lodging = "Yes"
    elif op == 2:
        lodging = "No" 
    else: 
        raise AttributeError("Atributo inválido")    
    return lodging

def lodging() -> str:
    data: list = fetchData("lodging")
    showData(data)
    lodging: str = getUserInput()
    return lodging