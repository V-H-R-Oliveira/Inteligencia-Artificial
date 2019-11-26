from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mFruiting Bodies: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Absent", 2: "Present"}
    return options.get(op, None)
def fruitingBodies() -> str:
    data: list = fetchData("fruiting_bodies")
    showData(data)
    fruitingBodies: str = getUserInput()
    return fruitingBodies