from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mSclerotia: \x1b[0m"))

    if op == 0:
        sclerotia = "Desconhecido"
    elif op == 1:
        sclerotia = "Absent"
    elif op == 2:
        sclerotia = "Present"
    else: 
        raise AttributeError("Atributo inválido")    
    return sclerotia

def sclerotia() -> str:
    data: list = fetchData("sclerotia")
    showData(data)
    sclerotia: str = getUserInput()
    return sclerotia