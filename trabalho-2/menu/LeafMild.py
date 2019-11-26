from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mLeaf mild: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Absent", 2: "Upper_surf", 3: "Lower_surf"}
    return options.get(op, None)

def leafMild() -> str:
    data: list = fetchData("leaf_mild")
    showData(data)
    leafMild: str = getUserInput()
    return leafMild