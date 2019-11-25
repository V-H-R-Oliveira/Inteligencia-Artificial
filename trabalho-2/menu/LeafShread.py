from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mLeaf shread: \x1b[0m"))

    if op == 0:
        leafShread = "Desconhecido"
    elif op == 1:
        leafShread = "absent"
    elif op == 2:
        leafShread = "Present"  
    else: 
        raise AttributeError("Atributo inválido")    
    return leafShread

def leafShread() -> str:
    data: list = fetchData("leaf_shread")
    showData(data)
    leafShread: str = getUserInput()
    return leafShread