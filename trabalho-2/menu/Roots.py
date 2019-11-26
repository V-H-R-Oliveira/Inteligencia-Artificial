from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mRoots: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Norm", 2: "Rotted", 3: "galls_cysts"}
    return options.get(op, None)

def roots() -> str:
    data: list = fetchData("roots")
    showData(data)
    roots: str = getUserInput()
    return roots