from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mMold growth: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Absent", 2: "Present"}
    return options.get(op, None)

def moldGrowth() -> str:
    data: list = fetchData("mold_growth")
    showData(data)
    moldGrowth: str = getUserInput()
    return moldGrowth