from menu.AreaDamaged import areaDamaged
from menu.CankerLesion import cankerLesion

if __name__ == "__main__":
    lista: list = []
    areaD: str = areaDamaged()
    lista.append(areaD)
    cankerL: str = cankerLesion()
    lista.append(cankerL)
    print(lista)