from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mTemp: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "lt_norm", 2: "norm", 3: "gt_norm"}
    return options.get(op, None)

def temp() -> str:
    data: list = fetchData("temp")
    showData(data)
    temp: str = getUserInput()
    return temp