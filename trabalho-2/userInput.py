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
from menu.Roots import roots
from menu.Sclerotia import sclerotia
from menu.Seed import seed
from menu.SeedDiscolor import seedDiscolor
from menu.SeedSize import seedSize
from menu.SeedTmt import seedTmt
from menu.Severity import severity
from menu.Shriveling import shriveling
from menu.Stem import stem
from menu.StemCankers import stemCankers
from menu.Temp import temp

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
    rootss: str = roots()
    lista.append(rootss)
    sclerotias: str = sclerotia()
    lista.append(sclerotias)
    seeds: str = seed()
    lista.append(seeds)
    seedDiscolors: str = seedDiscolor()
    lista.append(seedDiscolors)
    seedSizes: str = seedSize()
    lista.append(seedSizes)
    seedTmts: str = seedTmt()
    lista.append(seedTmts)
    severitys: str = severity()
    lista.append(severitys)
    shrivelings: str = shriveling()
    lista.append(shrivelings)
    stems: str = stem()
    lista.append(stems)
    stemCankerss: str = stemCankers()
    lista.append(stemCankerss)
    temps: str = temp()
    lista.append(temps)
    return lista