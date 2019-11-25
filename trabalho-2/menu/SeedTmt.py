from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mSeed Tmt: \x1b[0m"))

    if op == 0:
        seedTmt = "Desconhecido"
    elif op == 1:
        seedTmt = "none"
    elif op == 2:
        seedTmt = "fungicida"
    elif op == 3:
        seedTmt = "Outros"
    else: 
        raise AttributeError("Atributo inválido")    
    return seedTmt

def seedTmt() -> str:
    data: list = fetchData("seed_tmt")
    showData(data)
    seedTmt: str = getUserInput()
    return seedTmt