from Persistence import Persistence

def fetchData() -> list:
    dbHandler: Persistence = Persistence()
    dbHandler.connect()
    data: list = dbHandler.fetchAtributos("fruiting_bodies")
    return data

def percorrerDados(data: list):
    for index, element in enumerate(data):
        print("\x1b[1m", index, "|" ,element[0], "\x1b[0m")
        print("--------------------")

def getUserInput() -> str:
    op: int = int(input("\x1b[33mFruiting Bodies: \x1b[0m"))

    if op == 0:
        fruitingBodies = "Desconhecido"
    elif op == 1:
        fruitingBodies = "Absent"
    elif op == 2:
        fruitingBodies = "Present"
    else: 
        raise AttributeError("Atributo inválido")    
    return fruitingBodies

def fruitingBodies() -> str:
    data: list = fetchData()
    percorrerDados(data)
    fruitingBodies: str = getUserInput()
    return fruitingBodies