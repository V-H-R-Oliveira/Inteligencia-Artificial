from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mStem Cankers: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Absent", 2: "below_soil", 3: "Above_soil", 4: "Above_sec_nde"}
    return options.get(op, None)

def stemCankers() -> str:
    data: list = fetchData("stem_cankers")
    showData(data)
    stemCankers: str = getUserInput()
    return stemCankers