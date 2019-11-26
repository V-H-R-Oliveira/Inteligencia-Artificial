from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mInt discolor: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "None", 2: "Brown", 3: "Black"}
    return options.get(op, None)

def intDiscolor() -> str:
    data: list = fetchData("int_discolor")
    showData(data)
    intDiscolor: str = getUserInput()
    return intDiscolor