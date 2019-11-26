from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mPlant growth: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Norm", 2: "Abnorm"}
    return options.get(op, None)

def plantGrowth() -> str:
    data: list = fetchData("plant_growth")
    showData(data)
    plantGrowth: str = getUserInput()
    return plantGrowth