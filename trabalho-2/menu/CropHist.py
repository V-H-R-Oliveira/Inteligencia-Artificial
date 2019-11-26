from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mCrop Hist: \x1b[0m"))
    options: dict = {0: "Desconhecido", 1: "diff_1st_year", 
    2: "same_1st_yr", 3: "same_lst_two_yrs", 4: "same_lst_sev_yrs"}
    return options.get(op, None)

def cropHist() -> str:
    data: list = fetchData("crop_hist")
    showData(data)
    cropHist: str = getUserInput()
    return cropHist