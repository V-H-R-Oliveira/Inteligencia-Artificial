from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mSclerotia: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Absent", 2: "Present"}
    return options.get(op, None)

def sclerotia() -> str:
    data: list = fetchData("sclerotia")
    showData(data)
    sclerotia: str = getUserInput()
    return sclerotia