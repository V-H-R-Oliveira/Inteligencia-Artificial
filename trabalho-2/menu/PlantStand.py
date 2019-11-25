from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mPlant stand: \x1b[0m"))

    if op == 0:
        plantStand = "Desconhecido"
    elif op == 1:
        plantStand = "Normal"
    elif op == 2:
        plantStand = "lt_normal" 
    else: 
        raise AttributeError("Atributo inválido")    
    return plantStand

def plantStand() -> str:
    data: list = fetchData("plant_stand")
    showData(data)
    plantStand: str = getUserInput()
    return plantStand