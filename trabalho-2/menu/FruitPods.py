from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mFruit Pods: \x1b[0m"))

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
    data: list = fetchData("fruit_pods")
    showData(data)
    fruitPods: str = getUserInput()
    return fruitPods