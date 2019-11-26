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
    casos: list = [
        areaDamaged, cankerLesion, cropHist, date, externalDecay, 
        fruitSpots, fruitingBodies, fruitPods, germination, hail, intDiscolor,
        leafMalf, leafMild, leafShread, leafspotsHalo, leafspotSize, leafspotsMarg, 
        leaves, lodging, moldGrowth, mycelium, plantGrowth, plantStand, precip, roots, 
        sclerotia, seed,seedDiscolor,seedSize,seedTmt,severity, shriveling, stem, stemCankers, temp
        ]

    respostas: list = []
    for element in casos:
        respostas.append(element())
    return respostas