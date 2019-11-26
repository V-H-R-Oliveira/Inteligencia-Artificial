from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mSeed Size: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Norm", 2: "lt_norm"}
    return options.get(op, None)

def seedSize() -> str:
    data: list = fetchData("seed_size")
    showData(data)
    seedSize: str = getUserInput()
    return seedSize