from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mRoots: \x1b[0m"))

    if op == 0:
        roots = "Desconhecido"
    elif op == 1:
        roots = "Norm"
    elif op == 2:
        roots = "Rotted"
    elif op == 3:
        roots = "galls_cysts"
    else: 
        raise AttributeError("Atributo inválido")    
    return roots

def roots() -> str:
    data: list = fetchData("roots")
    showData(data)
    roots: str = getUserInput()
    return roots