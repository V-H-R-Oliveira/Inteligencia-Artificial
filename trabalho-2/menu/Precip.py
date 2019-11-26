from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mPrecip: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "lt_normal", 2: "Normal", 3: "gt_normal"}
    return options.get(op, None)

def precip() -> str:
    data: list = fetchData("precip")
    showData(data)
    precip: str = getUserInput()
    return precip