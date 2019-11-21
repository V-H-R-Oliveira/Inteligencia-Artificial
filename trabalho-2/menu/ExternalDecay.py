from Persistence import Persistence

def fetchData() -> list:
    dbHandler: Persistence = Persistence()
    dbHandler.connect()
    data: list = dbHandler.fetchAtributos("external_decay")
    return data

def percorrerDados(data: list):
    for index, element in enumerate(data):
        print("\x1b[1m", index, "|" ,element[0], "\x1b[0m")
        print("--------------------")

def getUserInput() -> str:
    op: int = int(input("\x1b[33mExternal Decay: \x1b[0m"))

    if op == 0:
        externalDecay = "Desconhecido"
    elif op == 1:
        externalDecay = "Absent"
    elif op == 2:
        externalDecay = "firm_and_dry"
    elif op == 3:
        externalDecay = "watery"
    else: 
        raise AttributeError("Atributo inválido")    
    return externalDecay

def externalDecay() -> str:
    data: list = fetchData()
    percorrerDados(data)
    externalDecay: str = getUserInput()
    return externalDecay