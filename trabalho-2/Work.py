from Persistence import Persistence
from userInput import userInput
from Similaridade import Similaridade

LABELS: list = ["area_damaged", "canker_lesion", "crop_hist", "date", "external_decay", "fruit_spots", 
"fruiting_bodies", "fruit_pods", "germination", "hail", "int_discolor", "leaf_malf", "leaf_mild",
"leaf_shread", "leafspots_halo", 
"leafspot_size", "leafspots_marg", "leaves", "lodging", 
"mold_growth", "mycelium", "plant_growth", "plant_stand", 
"precip", "roots", "sclerotia", "seed", "seed_discolor", 
"seed_size", "seed_tmt", "severity", 
"shriveling", "stem", "stem_cankers", "temp"]

dbHandler: Persistence = Persistence()
dbHandler.connect()

def fetchCasos() -> list:
    casos: list = dbHandler.fetchCasos()
    return casos

# função que calcula a similaridade local de todos os caso com o caso do usuário
def local() -> dict:
    casos: list = fetchCasos()
    # test_case: list = userInput() # descomente isto, para o usuário poder digitar :)
    test_case: list = ['scattered', 'Brown', 'same_1st_yr', 
    'Janeiro', 'firm_and_dry', 'Absent', 'Present', 
    'Norm', '80_89%', 'Yes', 'Brown', 'Absent', 
    'Upper_surf', 'absent', 'yellow_halos', 'lt_1/8', 
    'no_w_s_marg', 'Norm', 'No', 'Absent', 'Present', 
    'Abnorm', 'Normal', 'Normal', 'galls_cysts', 'Present', 
    'Norm', 'Present', 'Norm', 'fungicida', 'severe', 'Absent', 
    'Abnorm', 'Above_soil', 'norm']
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
    
    return final

def showResults(results: list, label: str):
    print("\x1b[1m\x1b[4m\x1b[32m\t{}:\x1b[0m".format(label))
    print("|-------------------------------------------|")

    for index, result in enumerate(results):
        print("\t\x1b[1m\x1b[34mCaso nº {}\x1b[0m = \x1b[1m\x1b[4m{}%\x1b[0m".format(index + 1, result * 100))
        print("|-------------------------------------------|")

# função que calcula a similaridade global
def main():
   pesos: list = dbHandler.fetchPesosTable() 
   simLocal: dict = local()
   dbHandler.closeConnection()
   simGlobal: list = Similaridade.globall(simLocal, pesos)
   showResults(simGlobal, "Similaridade global")