from Persistence import Persistence

def fetchData(tablename: str) -> list:
    dbHandler: Persistence = Persistence()
    dbHandler.connect()
    data: list = dbHandler.fetchAtributos(tablename)
    return data
