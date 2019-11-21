from Persistence import Persistence

def fetchData() -> list:
    dbHandler: Persistence = Persistence()
    dbHandler.connect()
    data: list = dbHandler.fetchAtributos("canker_lesion")
    return data

def percorrerDados(data: list):
    for index, element in enumerate(data):
        print("\x1b[1m", index, "|" ,element[0], "\x1b[0m")
        print("--------------------")

def getUserInput() -> str:
    op: int = int(input("\x1b[33mCanker Lesion: \x1b[0m"))

    if op == 0:
        cankerLesion = "Desconhecido"
    elif op == 1:
        cankerLesion = "dna"
    elif op == 2:
        cankerLesion = "Brown"
    elif op == 3:
        cankerLesion = "dk_brown"
    elif op == 4:
        cankerLesion = "tan"
    else: 
        raise AttributeError("Atributo inválido")    
    return cankerLesion

def cankerLesion() -> str:
    data: list = fetchData()
    percorrerDados(data)
    cankerLesion: str = getUserInput()
    return cankerLesion