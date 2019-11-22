from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[33mArea Damage: \x1b[0m"))

    if op == 0:
        areaDamage = "Desconhecido"
    elif op == 1:
        areaDamage = "scatterred"
    elif op == 2:
        areaDamage = "low_areas"
    elif op == 3:
        areaDamage = "upper_areas"
    elif op == 4:
        areaDamage = "while_field"
    else: 
        raise AttributeError("Atributo inválido")    
    return areaDamage

def areaDamaged() -> str:
    print("\x1b[32m Sistema RBC para classificação de doenças de Soja \x1b[0m")
    print('------------------------------------------------------------------')
    data: list = fetchData("area_damaged")
    showData(data)
    areaDamaged: str = getUserInput()
    return areaDamaged