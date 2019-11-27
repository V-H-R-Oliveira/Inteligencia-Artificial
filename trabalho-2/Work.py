from Persistence import Persistence
from userInput import userInput
from Similaridade import Similaridade
import time

LABELS: list = ["area_damaged", "canker_lesion", "crop_hist", 
"date", "external_decay", "fruit_spots", 
"fruiting_bodies", "fruit_pods", "germination", 
"hail", "int_discolor", "leaf_malf",
"leaf_mild", "leaf_shread", "leafspots_halo", 
"leafspot_size", "leafspots_marg", "leaves", 
"lodging", "mold_growth", "mycelium", 
"plant_growth", "plant_stand", "precip", 
"roots", "sclerotia", "seed", 
"seed_discolor", "seed_size", "seed_tmt", 
"severity", "shriveling", "stem", 
"stem_cankers", "temp"]

dbHandler: Persistence = Persistence()

def fetchCasos() -> list:
    casos: list = dbHandler.fetchCasos()
    return casos

def extractDoencas(casos: list) -> list:
    doencas: list = []
    for index, caso in enumerate(casos):
        doencas.append(casos[index][1])
    return doencas

# função que calcula a similaridade local de todos os caso com o caso do usuário
def local() -> tuple:
    casos: list = fetchCasos()
    doencas: list = extractDoencas(casos)
    test_case: list = userInput()
    aux: int = 2
    simLocal: list = []
    final: dict = {}

    for index, caso in enumerate(casos):
        for index_labels, label in enumerate(LABELS):
            pesos: list = dbHandler.fetchPesos(label)
            if "?" in pesos[0]:
                pesos[0] = (0, 'Desconhecido')
            dicPesos: dict = dict(((v,int(k)) for k,v in dict(pesos).items()))
            res: float = Similaridade.local(max(dicPesos.values()), min(dicPesos.values()), dicPesos[test_case[index_labels]], int(dicPesos[casos[index][aux]]))
            simLocal.append(res)
            aux += 1
        aux = 2
        tmp = {casos[index][0]: list(simLocal)}
        final.update(tmp)
        simLocal.clear()
    
    return (final, test_case, doencas)

def showResults(results: list, doencas: list):
    lista: list = list(zip(results, doencas))
    lista.sort(key=lambda e: e[0], reverse=True)
    print(sep="\n\n")
    print("\t\t\t\t\x1b[1m\x1b[4m\x1b[32mSimilaridade Global ordenada por ordem decrescente dos valores:\x1b[0m")
    print("|--------------------------------------------------------------------------------|")

    for index, result in enumerate(lista):
        if result[0] != 100:
            if index < 10:
                print("\t\x1b[1m\x1b[34mCaso nº {} \x1b[1m\x1b[33m[{}]\x1b[0m = \x1b[1m\x1b[4m\x1b[32m{}%\x1b[0m".format(index + 1, result[1], result[0]))
            elif index >= 10 and index < 20:
                print("\t\x1b[1m\x1b[34mCaso nº {} \x1b[1m\x1b[33m[{}]\x1b[0m = \x1b[1m\x1b[4m\x1b[33m{}%\x1b[0m".format(index + 1, result[1], result[0]))
            else:
                print("\t\x1b[1m\x1b[34mCaso nº {} \x1b[1m\x1b[33m[{}]\x1b[0m = \x1b[1m\x1b[47m\x1b[31m{}%\x1b[0m".format(index + 1, result[1], result[0]))
            print("|--------------------------------------------------------------------------------|")
            time.sleep(0.3)
        else:
            print("\t\x1b[5m\x1b[1m\x1b[34mCaso nº {} \x1b[1m\x1b[33m[{}]\x1b[0m = \x1b[1m\x1b[4m{}%\x1b[0m".format(index + 1, result[1], result[0]))
            print("|--------------------------------------------------------------------------------|")
            break
        
def verifyFullSim(simGlobal: list) -> bool:
    simGlobal.sort(reverse=True)
    if simGlobal[0] == 100:
        return False
    return True

def insertCasee(simLocal: tuple, userCase: list):
    nomeDoenca: str = input("\x1b[1m\x1b[32mInforme o nome do caso:\x1b[0m ")
    index: int = len(simLocal[0]) + 1
    userCase.insert(0, index)
    userCase.insert(1, nomeDoenca)
    dbHandler.insertCase(tuple(userCase))
    print("\x1b[1m\x1b[32mO seu caso foi inserido na base com sucesso\x1b[0m")

def updateCaso(simLocal: tuple, userCase: list):
    idCaso: int = int(input("\x1b[1m\x1b[32mInforme o id do caso:\x1b[0m "))
    dbHandler.updateCase(tuple(userCase), idCaso, LABELS)
    print("\x1b[1m\x1b[32mO caso foi atualizado\x1b[0m")

def displayCasos():
    casos: list = dbHandler.fetchCasosByPK()
    print()
    print("\t\x1b[1m\x1b[32mCasos disponíveis:\x1b[0m")
    print("|--------------------------------------------------------------------------------|")
    
    for caso in casos:
        print("\t\x1b[1m\x1b[34m{} -> \x1b[33m{}\x1b[0m".format(caso[0], caso[1]))
        print("|--------------------------------------------------------------------------------|")
        time.sleep(0.2)

def main():
    dbHandler.connect()
    pesos: list = dbHandler.fetchPesosTable() 
    simLocal: tuple = local()
    userCase: list = simLocal[1]
    simGlobal: list = Similaridade.globall(simLocal[0], pesos)
    showResults(simGlobal, simLocal[2])
    
    print()
    if verifyFullSim(simGlobal):
        op: int = int(input("\x1b[1m\x1b[33mVocê deseja atualizar ou inserir o caso \x1b[1m\x1b[32m{}\x1b[33m na base[1/2]:\x1b[0m ".format(userCase)))
        if op == 1:
            displayCasos()
            updateCaso(simLocal, userCase)
        elif op == 2:
            insertCasee(simLocal, userCase)
        else:
            dbHandler.closeConnection()
            raise AttributeError("\x1b[1m\x1b[31mOpção inválida\x1b[0m")
        dbHandler.closeConnection()
    else:
        dbHandler.closeConnection()
        print("\x1b[1m\x1b[31m Similaride global total foi encontrada\x1b[0m")