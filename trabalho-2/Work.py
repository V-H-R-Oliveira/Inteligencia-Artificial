from Persistence import Persistence
from userInput import userInput
from SimLocal import SimLocal

LABELS: list = ["area_damaged", "canker_lesion", "crop_hist", "date", "external_decay", "fruit_spots", 
"fruiting_bodies", "fruit_pods", "germination", "hail", "int_discolor", "leaf_malf", "leaf_mild",
"leaf_shread", "leafspots_halo", 
"leafspot_size", "leafspots_marg", "leaves", "lodging", 
"mold_growth", "mycelium", "plant_growth", "plant_stand", 
"precip", "roots", "sclerotia", "seed", "seed_discolor", 
"seed_size", "seed_tmt", "severity", 
"shriveling", "stem", "stem_cankers", "temp"]

# função que calcula a similaridade local de todos os caso com o caso do usuário

dbHandler: Persistence = Persistence()
dbHandler.connect()


def fetchCasos() -> list:
    casos: list = dbHandler.fetchCasos()
    return casos

# test case irá vir do userInput
def test():
    casos: list = fetchCasos()
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

    for index, caso in enumerate(casos):
        print("[Base] Caso {} - {}".format(casos[index][0], casos[index][1]))
        for index_labels, label in enumerate(LABELS):
            pesos: list = dbHandler.fetchPesos(label)
            # print(label, index_labels, pesos)
            # print(label)
            if "?" in pesos[0]:
                pesos[0] = (0, 'Desconhecido')
            dicPesos: dict = dict(((v,int(k)) for k,v in dict(pesos).items()))
            # print(pesos, dicPesos, test_case[index_labels], casos[index][aux], dicPesos[test_case[index_labels]], dicPesos[casos[index][aux]], sep="\n")
            res: float = SimLocal.calc(max(dicPesos.values()), min(dicPesos.values()), dicPesos[test_case[index_labels]], int(dicPesos[casos[index][aux]]))
            simLocal.append(res)
            aux += 1
        aux = 2
    
    print(len(simLocal))
    dbHandler.closeConnection()

test()