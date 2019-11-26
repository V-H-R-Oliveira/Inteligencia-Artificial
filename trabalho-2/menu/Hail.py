from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mHail: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Yes", 2: "No"}
    return options.get(op, None)

def hail() -> str:
    data: list = fetchData("hail")
    showData(data)
    hail: str = getUserInput()
    return hail