from Persistence import Persistence

def fetchData() -> list:
    dbHandler: Persistence = Persistence()
    dbHandler.connect()
    data: list = dbHandler.fetchAtributos("fruit_spots")
    return data

def percorrerDados(data: list):
    for index, element in enumerate(data):
        print("\x1b[1m", index, "|" ,element[0], "\x1b[0m")
        print("--------------------")

def getUserInput() -> str:
    op: int = int(input("\x1b[33mFruit Spots: \x1b[0m"))

    if op == 0:
        fruitSpots = "Desconhecido"
    elif op == 1:
        fruitSpots = "Absent"
    elif op == 2:
        fruitSpots = "Colored"
    elif op == 3:
        fruitSpots = "Brow-w/blk_specks"
    elif op == 4:
        fruitSpots = "Distort"
    elif op == 5:
        fruitSpots = "dna"
    else: 
        raise AttributeError("Atributo inválido")    
    return fruitSpots

def fruitSpots() -> str:
    data: list = fetchData()
    percorrerDados(data)
    fruitSpots: str = getUserInput()
    return fruitSpots