from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mSeverity: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Minor", 2: "pot_severe", 3: "severe"}
    return options.get(op, None)

def severity() -> str:
    data: list = fetchData("severity")
    showData(data)
    severity: str = getUserInput()
    return severity