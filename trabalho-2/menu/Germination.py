from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mGermination: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "90_100%", 2: "80_89%", 3: "lt_80%"}
    return options.get(op, None)

def germination() -> str:
    data: list = fetchData("germination")
    showData(data)
    germination: str = getUserInput()
    return germination