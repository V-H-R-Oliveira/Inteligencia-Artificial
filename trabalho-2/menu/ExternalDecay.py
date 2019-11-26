from menu.fetchData import fetchData

def percorrerDados(data: list):
    for index, element in enumerate(data):
        print("\x1b[1m", index, "|" ,element[0], "\x1b[0m")
        print("--------------------")

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mExternal Decay: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Absent", 2: "firm_and_dry", 3: "watery"}
    return options.get(op, None)

def externalDecay() -> str:
    data: list = fetchData("external_decay")
    percorrerDados(data)
    externalDecay: str = getUserInput()
    return externalDecay