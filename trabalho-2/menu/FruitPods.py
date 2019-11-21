from Persistence import Persistence

def fetchData() -> list:
    dbHandler: Persistence = Persistence()
    dbHandler.connect()
    data: list = dbHandler.fetchAtributos("fruit_pods")
    return data

def percorrerDados(data: list):
    for index, element in enumerate(data):
        print("\x1b[1m", index, "|" ,element[0], "\x1b[0m")
        print("--------------------")

def getUserInput() -> str:
    op: int = int(input("\x1b[33mFruit Pods: \x1b[0m"))

    if op == 0:
        fruitPods = "Desconhecido"
    elif op == 1:
        fruitPods = "Norm"
    elif op == 2:
        fruitPods = "Diseased"
    elif op == 3:
        fruitPods = "few_present"
    elif op == 4:
        fruitPods = "dna"
    else: 
        raise AttributeError("Atributo inválido")    
    return fruitPods

def fruitPods() -> str:
    data: list = fetchData()
    percorrerDados(data)
    fruitPods: str = getUserInput()
    return fruitPods