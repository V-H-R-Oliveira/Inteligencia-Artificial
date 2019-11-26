from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mDate: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5:"Maio",
    6: "Junho", 7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"}
    return options.get(op, None)
    
def date() -> str:
    data: list = fetchData("date")
    showData(data)
    date: str = getUserInput()
    return date