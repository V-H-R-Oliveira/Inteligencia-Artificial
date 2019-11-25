from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mStem Cankers: \x1b[0m"))

    if op == 0:
        stemCankers = "Desconhecido"
    elif op == 1:
        stemCankers = "Absent"
    elif op == 2:
        stemCankers = "below_soil"
    elif op == 3:
        stemCankers = "Above_soil"
    elif op == 4:
        stemCankers = "Above_sec_nde"  
    else: 
        raise AttributeError("Atributo inválido")    
    return stemCankers

def stemCankers() -> str:
    data: list = fetchData("stem_cankers")
    showData(data)
    stemCankers: str = getUserInput()
    return stemCankers