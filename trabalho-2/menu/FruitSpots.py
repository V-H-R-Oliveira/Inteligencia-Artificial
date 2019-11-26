from menu.showData import showData
from menu.fetchData import fetchData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mFruit Spots: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Absent", 2: "Colored", 3: "Brown_w/blk_specks", 4: "Distort", 5: "dna"}
    return options.get(op, None)

def fruitSpots() -> str:
    data: list = fetchData("fruit_spots")
    showData(data)
    fruitSpots: str = getUserInput()
    return fruitSpots