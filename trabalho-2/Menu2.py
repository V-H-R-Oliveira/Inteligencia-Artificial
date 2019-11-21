from menu.AreaDamaged import areaDamaged
from menu.CankerLesion import cankerLesion
from menu.CropHist import cropHist
from menu.Date import date
from menu.ExternalDecay import externalDecay
from menu.FruitSpots import fruitSpots
from menu.FruitingBodies import fruitingBodies
from menu.FruitPods import fruitPods

if __name__ == "__main__":
    lista: list = []
    areaD: str = areaDamaged()
    lista.append(areaD)
    cankerL: str = cankerLesion()
    lista.append(cankerL)
    cropH: str = cropHist()
    lista.append(cropH)
    date: str = date()
    lista.append(date)
    externalDecay: str = externalDecay()
    lista.append(externalDecay)
    fruitSpots: str = fruitSpots()
    lista.append(fruitSpots)
    fruitingBodies: str = fruitingBodies()
    lista.append(fruitingBodies)
    fruitPods: str = fruitPods()
    lista.append(fruitPods)
    print(lista)