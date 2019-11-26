from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mMycelium: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Absent", 2: "Present"}
    return options.get(op, None)

def mycelium() -> str:
    data: list = fetchData("mycelium")
    showData(data)
    mycelium: str = getUserInput()
    return mycelium