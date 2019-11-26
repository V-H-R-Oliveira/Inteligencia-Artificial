from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mArea Damage: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1:"scattered", 2: "low_areas", 3:"upper_areas", 4:"whole_field"}
    return options.get(op, None)


def areaDamaged() -> str:
    data: list = fetchData("area_damaged")
    showData(data)
    areaDamaged: str = getUserInput()
    return areaDamaged