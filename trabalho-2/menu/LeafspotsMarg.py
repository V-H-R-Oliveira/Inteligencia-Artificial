from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mLeafspots marg: \x1b[0m"))

    if op == 0:
        leafspotsMarg = "Desconhecido"
    elif op == 1:
        leafspotsMarg = "w_s_marg"
    elif op == 2:
        leafspotsMarg = "no_w_s_marg"
    elif op == 3:
        leafspotsMarg = "dna"     
    else: 
        raise AttributeError("Atributo inválido")    
    return leafspotsMarg

def leafspotsMarg() -> str:
    data: list = fetchData("leafspots_marg")
    showData(data)
    leafspotsMarg: str = getUserInput()
    return leafspotsMarg