from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mLeafspot size: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "lt_1/8", 2: "gt_1/8", 3: "dna"}
    return options.get(op, None)

def leafspotSize() -> str:
    data: list = fetchData("leafspot_size")
    showData(data)
    leafspotSize: str = getUserInput()
    return leafspotSize