class SimLocal(object):
    @staticmethod
    def calc(maior, menor, peso, coluna):
        return 1 - ((abs(peso - coluna)) / (maior - menor))