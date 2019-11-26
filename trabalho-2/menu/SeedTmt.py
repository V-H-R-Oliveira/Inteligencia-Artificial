from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mSeed Tmt: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "none", 2: "fungicida", 3: "Outros"}
    return options.get(op, None)

def seedTmt() -> str:
    data: list = fetchData("seed_tmt")
    showData(data)
    seedTmt: str = getUserInput()
    return seedTmt