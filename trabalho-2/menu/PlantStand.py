from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mPlant stand: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Normal", 2: "lt_normal"}
    return options.get(op, None)

def plantStand() -> str:
    data: list = fetchData("plant_stand")
    showData(data)
    plantStand: str = getUserInput()
    return plantStand