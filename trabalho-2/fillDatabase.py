from Pesos import Pesos
from Atributos import Atributos
from Casos import Casos
from Persistence import Persistence

if __name__ == "__main__": # executar uma vez para popular o banco de dados, após seguir os passos do README
    dbHandler: Persistence = Persistence()
    dbHandler.createSchema()
    pesos: Pesos = Pesos("pesos.csv")
    atributos: Atributos = Atributos("atributos.csv")
    casos: Casos = Casos("casos.csv")
    pesos.persist()
    atributos.persist()
    casos.persist()
    print("\x1b[1m\x1b[5m\x1b[32mO Banco de dados foi criado com sucesso!!!\x1b[0m")
