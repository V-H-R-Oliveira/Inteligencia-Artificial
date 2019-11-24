from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mSeverity: \x1b[0m"))

    if op == 0:
        severity = "Desconhecido"
    elif op == 1:
        severity = "Minor"
    elif op == 2:
        severity = "pot_severe"
    elif op == 3:
        severity = "severe"
    else: 
        raise AttributeError("Atributo inválido")    
    return severity

def severity() -> str:
    data: list = fetchData("severity")
    showData(data)
    severity: str = getUserInput()
    return severity