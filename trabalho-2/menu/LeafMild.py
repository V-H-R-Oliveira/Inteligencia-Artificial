from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mLeaf mild: \x1b[0m"))

    if op == 0:
        leafMild = "Desconhecido"
    elif op == 1:
        leafMild = "Absent"
    elif op == 2:
        leafMild = "Upper_surf"
    elif op == 3:
        leafMild = "Lower_surf"   
    else: 
        raise AttributeError("Atributo inválido")    
    return leafMild

def leafMild() -> str:
    data: list = fetchData("leaf_mild")
    showData(data)
    leafMild: str = getUserInput()
    return leafMild