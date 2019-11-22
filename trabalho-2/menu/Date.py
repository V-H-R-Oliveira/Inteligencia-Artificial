from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mDate: \x1b[0m"))

    if op == 0:
        date = "Desconhecido"
    elif op == 1:
        date = "Janeiro"
    elif op == 2:
        date = "Fevereiro"
    elif op == 3:
        date = "Março"
    elif op == 4:
        date = "Abril"
    elif op == 5:
        date = "Maio"
    elif op == 6:
        date = "Junho"
    elif op == 7:
        date = "Julho"
    elif op == 8:
        date = "Agosto"
    elif op == 9:
        date = "Setembro"
    elif op == 10:
        date = "Outubro"
    elif op == 11:
        date = "Novembro"
    elif op == 12:
        date = "Dezembro"
    else: 
        raise AttributeError("Atributo inválido")    
    return date

def date() -> str:
    data: list = fetchData("date")
    showData(data)
    date: str = getUserInput()
    return date