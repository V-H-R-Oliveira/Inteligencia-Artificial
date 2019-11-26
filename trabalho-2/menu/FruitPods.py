from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mFruit Pods: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Norm", 2: "Diseased", 3: "few_present", 4: "dna"}
    return options.get(op, None)

def fruitPods() -> str:
    data: list = fetchData("fruit_pods")
    showData(data)
    fruitPods: str = getUserInput()
    return fruitPods