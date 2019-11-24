from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mShriveling: \x1b[0m"))

    if op == 0:
        shriveling = "Desconhecido"
    elif op == 1:
        shriveling = "Absent"
    elif op == 2:
        shriveling = "Present"
    else: 
        raise AttributeError("Atributo inválido")    
    return shriveling

def shriveling() -> str:
    data: list = fetchData("shriveling")
    showData(data)
    shriveling: str = getUserInput()
    return shriveling