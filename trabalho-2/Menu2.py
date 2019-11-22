from menu.AreaDamaged import areaDamaged
from menu.CankerLesion import cankerLesion
from menu.CropHist import cropHist
from menu.Date import date
from menu.ExternalDecay import externalDecay
from menu.FruitSpots import fruitSpots
from menu.FruitingBodies import fruitingBodies
from menu.FruitPods import fruitPods
from menu.Germination import germination
from menu.Hail import hail
from menu.IntDiscolor import intDiscolor
from menu.LeafMalf import leafMalf
from menu.LeafMild import leafMild
from menu.LeafShread import leafShread
from menu.LeafspotsHalo import leafspotsHalo
from menu.LeafspotSize import leafspotSize
from menu.LeafspotsMarg import leafspotsMarg
from menu.Leaves import leaves

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
    germination: str = germination()
    lista.append(germination)
    hail: str = hail()
    lista.append(hail)
    intDiscolor: str = intDiscolor()
    lista.append(intDiscolor)
    leafMalf: str = leafMalf()
    lista.append(leafMalf)
    leafMild: str = leafMild()
    lista.append(leafMild)
    leafShread: str = leafShread()
    lista.append(leafShread)
    leafspotsHalo: str = leafspotsHalo()
    lista.append(leafspotsHalo)
    leafspotSize: str = leafspotSize()
    lista.append(leafspotSize)
    leafspotsMarg: str = leafspotsMarg()
    lista.append(leafspotsMarg)
    leaves: str = leaves()
    lista.append(leaves)
    print(lista)