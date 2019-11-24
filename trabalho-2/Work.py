from Persistence import Persistence

# função que calcula a similaridade local de todos os caso com o caso do usuário

dbHandler: Persistence = Persistence()
dbHandler.connect()


def fetchCasos() -> list:
    casos: list = dbHandler.fetchCasos()
    return casos


atrib: list = dbHandler.fetchPesos("area_damaged")
print(atrib)