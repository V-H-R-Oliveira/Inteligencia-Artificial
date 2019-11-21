from Persistence import Persistence

def fetchData() -> list:
    dbHandler: Persistence = Persistence()
    dbHandler.connect()
    data: list = dbHandler.fetchAtributos("date")
    return data

def percorrerDados(data: list):
    for index, element in enumerate(data):
        print("\x1b[1m", index, "|" ,element[0], "\x1b[0m")
        print("--------------------")

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
    data: list = fetchData()
    percorrerDados(data)
    date: str = getUserInput()
    return date