from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mLeafspots halo: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "absent", 2: "yellow_halos", 3: "no_yellow_halos"}
    return options.get(op, None)

def leafspotsHalo() -> str:
    data: list = fetchData("leafspots_halo")
    showData(data)
    leafspotsHalo: str = getUserInput()
    return leafspotsHalo