from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mCanker Lesion: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "dna", 2: "Brown", 3: "dk_brown_blk", 4: "tan"}
    return options.get(op, None)
  

def cankerLesion() -> str:
    data: list = fetchData("canker_lesion")
    showData(data)
    cankerLesion: str = getUserInput()
    return cankerLesion