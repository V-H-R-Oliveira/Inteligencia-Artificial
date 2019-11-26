from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mLeaf shread: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "absent", 2: "Present"}
    return options.get(op, None)

def leafShread() -> str:
    data: list = fetchData("leaf_shread")
    showData(data)
    leafShread: str = getUserInput()
    return leafShread