from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mSeed: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Norm", 2: "Abnorm"}
    return options.get(op, None)

def seed() -> str:
    data: list = fetchData("seed")
    showData(data)
    seed: str = getUserInput()
    return seed