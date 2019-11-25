from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mMold growth: \x1b[0m"))

    if op == 0:
        moldGrowth = "Desconhecido"
    elif op == 1:
        moldGrowth = "Absent"
    elif op == 2:
        moldGrowth = "Present" 
    else: 
        raise AttributeError("Atributo inválido")    
    return moldGrowth

def moldGrowth() -> str:
    data: list = fetchData("mold_growth")
    showData(data)
    moldGrowth: str = getUserInput()
    return moldGrowth