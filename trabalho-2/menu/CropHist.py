from menu.fetchData import fetchData
from menu.showData import showData

def getUserInput() -> str:
    op: int = int(input("\x1b[1m\x1b[33mCrop Hist: \x1b[0m"))

    if op == 0:
        cropHist = "Desconhecido"
    elif op == 1:
        cropHist = "diff_1st_year"
    elif op == 2:
        cropHist = "same_1st_yr"
    elif op == 3:
        cropHist = "same_lst_two_yrs"
    elif op == 4:
        cropHist = "same_lst_sev_yrs"
    else: 
        raise AttributeError("Atributo inválido")    
    return cropHist

def cropHist() -> str:
    data: list = fetchData("crop_hist")
    showData(data)
    cropHist: str = getUserInput()
    return cropHist