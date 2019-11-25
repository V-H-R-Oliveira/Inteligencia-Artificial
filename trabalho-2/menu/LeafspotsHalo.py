from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mLeafspots halo: \x1b[0m"))

    if op == 0:
        leafspotsHalo = "Desconhecido"
    elif op == 1:
        leafspotsHalo = "absent"
    elif op == 2:
        leafspotsHalo = "yellow_halos"
    elif op == 3:
        leafspotsHalo = "no_yellow_halos"   
    else: 
        raise AttributeError("Atributo inválido")    
    return leafspotsHalo

def leafspotsHalo() -> str:
    data: list = fetchData("leafspots_halo")
    showData(data)
    leafspotsHalo: str = getUserInput()
    return leafspotsHalo