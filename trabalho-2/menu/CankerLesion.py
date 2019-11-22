from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mCanker Lesion: \x1b[0m"))

    if op == 0:
        cankerLesion = "Desconhecido"
    elif op == 1:
        cankerLesion = "dna"
    elif op == 2:
        cankerLesion = "Brown"
    elif op == 3:
        cankerLesion = "dk_brown"
    elif op == 4:
        cankerLesion = "tan"
    else: 
        raise AttributeError("Atributo inválido")    
    return cankerLesion

def cankerLesion() -> str:
    data: list = fetchData("canker_lesion")
    showData(data)
    cankerLesion: str = getUserInput()
    return cankerLesion