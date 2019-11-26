from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mLeafspots marg: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "w_s_marg", 2: "no_w_s_marg", 3: "dna"}
    return options.get(op, None)

def leafspotsMarg() -> str:
    data: list = fetchData("leafspots_marg")
    showData(data)
    leafspotsMarg: str = getUserInput()
    return leafspotsMarg