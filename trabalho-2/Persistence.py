import os, sqlite3

class Persistence(object):
    def __init__(self, dbName: str = "rbc.db"): 
        self.__dbName: str = os.getcwd() + "/{}".format(dbName)
        self.__conn: sqlite3 = None
    
    def connect(self):
        try:
            self.__conn: sqlite3 = sqlite3.connect(self.__dbName)
        except Exception as error:
            raise error
    
    def createSchema(self):
        with open(os.getcwd() + "/sql/createTables.sql", "r") as fd:
            schema: str = fd.read()
        try:
            self.connect()
            cursor = self.__conn.cursor()        
            cursor.executescript(schema)
            self.__conn.close()
        except Exception as error:
            self.__conn.rollback()
            self.__conn.close()
            raise error

    def insert(self, tableName: str, data: list):
        cursor = self.__conn.cursor()
        if tableName.lower() == "pesos":
            QUERY: str = "INSERT INTO pesos (id, atributo, peso) VALUES (?, ?, ?);"
            try:
                cursor.executemany(QUERY, data)
                self.__conn.commit()
            except Exception as error:
                self.__conn.rollback()
                self.__conn.close()
                raise error
        elif tableName.lower() == "atributos":
            QUERY: str = "INSERT INTO atributos (id, atributo, peso, valor) VALUES (?, ?, ?, ?);"
            try:
                cursor.executemany(QUERY, data)
                self.__conn.commit()
            except Exception as error:
                self.__conn.rollback()
                self.__conn.close()
                raise error
        elif tableName.lower() == "casos":
            QUERY: str = "INSERT INTO casos (id, desc_doenca, area_damaged, canker_lesion, crop_hist, case_date, external_decay, fruit_spots, fruiting_bodies, fruit_pods, germination, hail, int_discolor, leaf_malf, leaf_mild, leaf_shread, leafspots_halo, leafspot_size, leafspots_marg, leaves, lodging, mold_growth, mycelium, plant_growth, plant_stand, precip, roots, sclerotia, seed, seed_discolor, seed_size, seed_tmt, severity, shriveling, stem, stem_cankers, temp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
            try:
                cursor.executemany(QUERY, data)
                self.__conn.commit()
            except Exception as error:
                self.__conn.rollback()
                self.__conn.close()
                raise error
        else:
            self.__conn.rollback()
            self.__conn.close()
            raise AttributeError("O nome da tabela é inválido")
    
    def fetchAtributos(self, element: str) -> list:
        data: list = []
        cursor = self.__conn.cursor()
        QUERY: str = "SELECT valor FROM atributos WHERE atributo='{}';".format(element)
        try:
            cursor.execute(QUERY)
            self.__conn.commit()
            data = cursor.fetchall()
            return data
        except Exception as error:
            self.__conn.rollback()
            self.__conn.close()
            raise error
    
    def fetchCasos(self) -> list:
        data: list = []
        cursor = self.__conn.cursor()
        QUERY: str = "SELECT * FROM casos;"
        try:
            cursor.execute(QUERY)
            self.__conn.commit()
            data = cursor.fetchall()
            return data
        except Exception as error:
            self.__conn.rollback()
            self.__conn.close()
            raise error

    def fetchPesos(self, atributo: str) -> list:
        data: list = []
        cursor = self.__conn.cursor()
        QUERY: str = "SELECT peso, valor FROM atributos WHERE atributo=\'{}\';".format(atributo)
        try:
            cursor.execute(QUERY)
            self.__conn.commit()
            data = cursor.fetchall()
            return data
        except Exception as error:
            self.__conn.rollback()
            self.__conn.close()
            raise error
    
    def fetchPesosTable(self) -> list:
        data: list = []
        cursor = self.__conn.cursor()
        QUERY: str = "SELECT atributo, peso FROM pesos;"
        try:
            cursor.execute(QUERY)
            self.__conn.commit()
            data = cursor.fetchall()
            return data
        except Exception as error:
            self.__conn.rollback()
            self.__conn.close()
            raise error
    
    def insertCase(self, data: list):
        QUERY: str = "INSERT INTO casos (id, desc_doenca, area_damaged, canker_lesion, crop_hist, case_date, external_decay, fruit_spots, fruiting_bodies, fruit_pods, germination, hail, int_discolor, leaf_malf, leaf_mild, leaf_shread, leafspots_halo, leafspot_size, leafspots_marg, leaves, lodging, mold_growth, mycelium, plant_growth, plant_stand, precip, roots, sclerotia, seed, seed_discolor, seed_size, seed_tmt, severity, shriveling, stem, stem_cankers, temp) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);"
        cursor = self.__conn.cursor()
        try:
            cursor.execute(QUERY, data)
            self.__conn.commit()
        except Exception as error:
            self.__conn.rollback()
            self.__conn.close()
            raise error
    
    def fetchCasosByPK(self) -> list:
        cursor = self.__conn.cursor()
        QUERY: str = "SELECT id, desc_doenca FROM casos;"
        try:
            data: list = []
            cursor.execute(QUERY)
            self.__conn.commit()
            data = cursor.fetchall()
            return data
        except Exception as error:
            self.__conn.rollback()
            self.__conn.close()
            raise error
    
    # Peça de magia negra
    def __prepareQuery(self, data: list, idCaso: int, labels: list) -> str:
        labels[labels.index("date")] = "case_date"
        QUERY: str = "UPDATE casos SET "
        for index, item in enumerate(labels):
            if index < 34:
                QUERY += "{}=\'{}\',".format(item, data[index])
            else:
                QUERY += "{}=\'{}\'".format(item, data[index])
        QUERY += " WHERE id={};".format(idCaso)
        return QUERY

    def updateCase(self, data: list, idCaso: int, labels: list):
        QUERY: str = self.__prepareQuery(data, idCaso, labels)
        cursor = self.__conn.cursor()
        try:
            cursor.execute(QUERY)
            self.__conn.commit()
        except Exception as error:
            self.__conn.rollback()
            self.__conn.close()
            raise error

    def closeConnection(self):
        try:
            self.__conn.close()
        except Exception as error:
            raise error