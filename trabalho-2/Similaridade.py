class Similaridade(object):
    @staticmethod
    def local(maior: int, menor: int, peso: int, coluna: int) -> float:
        return 1 - ((abs(peso - coluna)) / (maior - menor))
    
    @staticmethod
    def globall(simLocal: dict, pesos: list) -> list:
        resultados: list = []
        somaPesos: int = 0
        somaSimLocal: int = 0
        
        for peso in pesos:
            somaPesos += peso[1]

        for sim in simLocal.values():
            for index, value in enumerate(sim):
                somaSimLocal += value * pesos[index][1]
            aux: float = (somaSimLocal / somaPesos) * 100
            resultados.append(aux)
            somaSimLocal = 0
        return resultados