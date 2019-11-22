from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mPlant growth: \x1b[0m"))

    if op == 0:
        plantGrowth = "Desconhecido"
    elif op == 1:
        plantGrowth = "Norm"
    elif op == 2:
        plantGrowth = "Abnorm" 
    else: 
        raise AttributeError("Atributo inválido")    
    return plantGrowth

def plantGrowth() -> str:
    data: list = fetchData("plant_growth")
    showData(data)
    plantGrowth: str = getUserInput()
    return plantGrowth