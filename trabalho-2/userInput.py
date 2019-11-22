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
from menu.Lodging import lodging
from menu.MoldGrowth import moldGrowth
from menu.Mycelium import mycelium
from menu.PlantGrowth import plantGrowth
from menu.PlantStand import plantStand
from menu.Precip import precip

def userInput() -> list:
    lista: list = []
    areaD: str = areaDamaged()
    lista.append(areaD)
    cankerL: str = cankerLesion()
    lista.append(cankerL)
    cropH: str = cropHist()
    lista.append(cropH)
    datee: str = date()
    lista.append(datee)
    externalDecayy: str = externalDecay()
    lista.append(externalDecayy)
    fruitSpotss: str = fruitSpots()
    lista.append(fruitSpotss)
    fruitingBodiess: str = fruitingBodies()
    lista.append(fruitingBodiess)
    fruitPodss: str = fruitPods()
    lista.append(fruitPodss)
    germinations: str = germination()
    lista.append(germinations)
    hails: str = hail()
    lista.append(hails)
    intDiscolors: str = intDiscolor()
    lista.append(intDiscolors)
    leafMalfs: str = leafMalf()
    lista.append(leafMalfs)
    leafMilds: str = leafMild()
    lista.append(leafMilds)
    leafShreads: str = leafShread()
    lista.append(leafShreads)
    leafspotsHalos: str = leafspotsHalo()
    lista.append(leafspotsHalos)
    leafspotSizes: str = leafspotSize()
    lista.append(leafspotSizes)
    leafspotsMargs: str = leafspotsMarg()
    lista.append(leafspotsMargs)
    leavess: str = leaves()
    lista.append(leavess)
    lodgings: str = lodging()
    lista.append(lodgings)
    moldGrowths: str = moldGrowth()
    lista.append(moldGrowths)
    myceliums: str = mycelium()
    lista.append(myceliums)
    plantGrowths: str = plantGrowth()
    lista.append(plantGrowths)
    plantStands: str = plantStand()
    lista.append(plantStands)
    precips: str = precip()
    lista.append(precips)

    return lista