from Persistence import Persistence

def fetchData() -> list:
    dbHandler: Persistence = Persistence()
    dbHandler.connect()
    data: list = dbHandler.fetchAtributos("area_damaged")
    return data

def percorrerDados(data: list):
    for index, element in enumerate(data):
        print("\x1b[1m", index, "|" ,element[0], "\x1b[0m")
        print("--------------------")

def getUserInput() -> str:
    op: int = int(input("\x1b[33mArea Damage: \x1b[0m"))

    if op == 0:
        areaDamage = "Desconhecido"
    elif op == 1:
        areaDamage = "scatterred"
    elif op == 2:
        areaDamage = "low-areas"
    elif op == 3:
        areaDamage = "upper-areas"
    elif op == 4:
        areaDamage = "while-field"
    else: 
        raise AttributeError("Atributo inválido")    
    return areaDamage

def areaDamaged() -> str:
    print("\x1b[32m Sistema RBC para classificação de doenças de Soja \x1b[0m")
    print('------------------------------------------------------------------')
    data: list = fetchData()
    percorrerDados(data)
    areaDamaged: str = getUserInput()
    return areaDamaged