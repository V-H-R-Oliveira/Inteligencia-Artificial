# import os, time

# def menu(pesos, atributos, casos):
#     print("Sistema RBC para classificação de doenças da Soja: ")
#  #area-damaged input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "area-damaged":
#             print(aux," - ",atributos[i][2])
#             aux+=1  
#     op = int(input("Area Damage: "))
#     if op == 1:
#         areaDamage = "Desconhecido"
#     elif op == 2:
#         areaDamage = "scatterred"
#     elif op == 3:
#         areaDamage = "low-areas"
#     elif op == 4:
#         areaDamage = "upper-areas"
#     elif op == 5:
#         areaDamage = "while-field"    
#     time.sleep(0.5)
#     os.system("clear")
# #canker-lesion input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "canker-lesion":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Canker Lesion: "))
#     if op == 1:
#         cankerLesion = "Desconhecido"
#     elif op == 2:
#         cankerLesion = "dna"
#     elif op == 3:
#         cankerLesion = "Brown"
#     elif op == 4:
#         cankerLesion = "dk-brown-blk"
#     elif op == 5:
#         cankerLesion = "tan"    
#     time.sleep(0.5)
#     os.system("clear")
#     #crop-hist input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "crop-hist":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Crop Hist: "))
#     if op == 1:
#         cropHist = "Desconhecido"
#     elif op == 2:
#         cropHist = "diff-1st-year"
#     elif op == 3:
#         cropHist = "same-1st-yr"
#     elif op == 4:
#         cropHist = "same-lst-two-yrs"
#     elif op == 5:
#         cropHist = "same-lst-sev-yrs"    
#     time.sleep(0.5)
#     os.system("clear")
#     #date input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "date":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Date: "))
#     if op == 1:
#         date = "Desconhecido"
#     elif op == 2:
#         date = "Janeiro"
#     elif op == 3:
#         date = "Fevereiro"
#     elif op == 4:
#         date = "Março"
#     elif op == 5:
#         date = "Abril"
#     elif op == 6:
#         date = "Maio"  
#     elif op == 7:
#         date = "Junho"  
#     elif op == 8:
#         date = "Julho"  
#     elif op == 9:
#         date = "Agosto"  
#     elif op == 10:
#         date = "Setembro"  
#     elif op == 11:
#         date = "Outubro"  
#     elif op == 12:
#         date = "Novembro"  
#     elif op == 13:
#         date = "Dezembro"       
#     time.sleep(0.5)
#     os.system("clear")    
#     #external decay input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "external decay":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("External Decay: "))
#     if op == 1:
#         externalDecay = "Desconhecido"
#     elif op == 2:
#         externalDecay = "Absent"
#     elif op == 3:
#         externalDecay = "firm-and-dry"
#     elif op == 4:
#         externalDecay = "watery"  
#     time.sleep(0.5)
#     os.system("clear")
#     #fruit spots input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "fruit spots":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Fruit Spots: "))
#     if op == 1:
#         fruitSpots = "Desconhecido"
#     elif op == 2:
#         fruitSpots = "Absent"
#     elif op == 3:
#         fruitSpots = "Colored"
#     elif op == 4:
#         fruitSpots = "Brow-w/blk-specks"
#     elif op == 5:
#         fruitSpots = "Distort"
#     elif op == 6:
#         fruitSpots = "dna"    
#     time.sleep(0.5)
#     os.system("clear")
#     #fruiting-bodies input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "fruiting-bodies":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Fruiting Bodies: "))
#     if op == 1:
#         cankerLesion = "Desconhecido"
#     elif op == 2:
#         cankerLesion = "Absent"
#     elif op == 3:
#         cankerLesion = "Present"
#     time.sleep(0.5)
#     os.system("clear")
#     #fruit-pods input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "fruit-pods":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Fruit Pods: "))
#     if op == 1:
#         fruitPods = "Desconhecido"
#     elif op == 2:
#         fruitPods = "Norm"
#     elif op == 3:
#         fruitPods = "Diseased"
#     elif op == 4:
#         fruitPods = "few-present"
#     elif op == 5:
#         fruitPods = "dna"    
#     time.sleep(0.5)
#     os.system("clear")
#     #germination input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "germination":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Germination: "))
#     if op == 1:
#         germination = "Desconhecido"
#     elif op == 2:
#         germination = "90-100%"
#     elif op == 3:
#         germination = "80-89%"
#     elif op == 4:
#         germination = "lt-80%" 
#     time.sleep(0.5)
#     os.system("clear")
#     #hail input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "hail":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Hail: "))
#     if op == 1:
#         hail = "Desconhecido"
#     elif op == 2:
#         hail = "Yes"
#     elif op == 3:
#         hail = "No" 
#     time.sleep(0.5)
#     os.system("clear")
#     #int-discolor input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "int-discolor":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Int Discolor: "))
#     if op == 1:
#         intDiscolor = "Desconhecido"
#     elif op == 2:
#         intDiscolor = "None"
#     elif op == 3:
#         intDiscolor = "Brown"
#     elif op == 4:
#         intDiscolor = "Black" 
#     time.sleep(0.5)
#     os.system("clear")
#     #leaf-malf input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "leaf-malf":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Leaf Malf: "))
#     if op == 1:
#         leafMalf = "Desconhecido"
#     elif op == 2:
#         leafMalf = "Absent"
#     elif op == 3:
#         leafMalf = "Present" 
#     time.sleep(0.5)
#     os.system("clear")
#     #leaf-mild input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "leaf-mild":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Leaf Mild: "))
#     if op == 1:
#         leafMild = "Desconhecido"
#     elif op == 2:
#         leafMild = "Absent"
#     elif op == 3:
#         leafMild = "Upper-surf"
#     elif op == 4:
#         leafMild = "Lower-surf"   
#     time.sleep(0.5)
#     os.system("clear")
#     #leaf-shread input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "leaf-shread":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Leaf Shread: "))
#     if op == 1:
#         leafShread = "Desconhecido"
#     elif op == 2:
#         leafShread = "Absent"
#     elif op == 3:
#         leafShread = "Present"  
#     time.sleep(0.5)
#     os.system("clear") 
#     #leafspots-halo input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "leafspots-halo":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Leafspots Halo: "))
#     if op == 1:
#         leafspotsHalo = "Desconhecido"
#     elif op == 2:
#         leafspotsHalo = "absent"
#     elif op == 3:
#         leafspotsHalo = "yellow-halos"
#     elif op == 4:
#         leafspotsHalo = "no-yellow-halos"   
#     time.sleep(0.5)
#     os.system("clear")
#     #leafspot-size input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "leafspot-size":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Leafspot Size: "))
#     if op == 1:
#         leafspotSize = "Desconhecido"
#     elif op == 2:
#         leafspotSize = "lt-1/8"
#     elif op == 3:
#         leafspotSize = "gt-1/8"
#     elif op == 4:
#         leafspotSize = "dna"  
#     time.sleep(0.5)
#     os.system("clear")
#     #leafspots-marg input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "leafspots-marg":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Leafspots Marg: "))
#     if op == 1:
#         leafspotsMarg = "Desconhecido"
#     elif op == 2:
#         leafspotsMarg = "w-s-marg"
#     elif op == 3:
#         leafspotsMarg = "no-w-s-marg"
#     elif op == 4:
#         leafspotsMarg = "dna"   
#     time.sleep(0.5)
#     os.system("clear")
#     #leaves input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "leaves":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Leaves: "))
#     if op == 1:
#         leaves = "Desconhecido"
#     elif op == 2:
#         leaves = "Norm"
#     elif op == 3:
#         leaves = "Abnorm"  
#     time.sleep(0.5)
#     os.system("clear")
#     #lodging input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "lodging":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Lodging: "))
#     if op == 1:
#         lodging = "Desconhecido"
#     elif op == 2:
#         lodging = "Yes"
#     elif op == 3:
#         lodging = "No"    
#     time.sleep(0.5)
#     os.system("clear")
#     #mold-growth input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "mold-growth":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Mold Growth: "))
#     if op == 1:
#         moldGrowth = "Desconhecido"
#     elif op == 2:
#         moldGrowth = "Absent"
#     elif op == 3:
#         moldGrowth = "Present"   
#     time.sleep(0.5)
#     os.system("clear")
#     #mycelium input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "mycelium":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Mycelium: "))
#     if op == 1:
#         mycelium = "Desconhecido"
#     elif op == 2:
#         mycelium = "Absent"
#     elif op == 3:
#         mycelium = "Present"
#     time.sleep(0.5)
#     os.system("clear")
#     #plant-growth input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "plant-growth":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Plant Growth: "))
#     if op == 1:
#         plantGrowth = "Desconhecido"
#     elif op == 2:
#         plantGrowth = "Norm"
#     elif op == 3:
#         plantGrowth = "Abnorm" 
#     time.sleep(0.5)
#     os.system("clear")
#     #plant-stand input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "plant-stand":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Plant Stand: "))
#     if op == 1:
#         plantStand = "Desconhecido"
#     elif op == 2:
#         plantStand = "Normal"
#     elif op == 3:
#         plantStand = "lt-normal" 
#     time.sleep(0.5)
#     os.system("clear")
#     #precip input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "precip":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Precip: "))
#     if op == 1:
#         precip = "Desconhecido"
#     elif op == 2:
#         precip = "lt-normal"
#     elif op == 3:
#         precip = "Normal"
#     elif op == 4:
#         precip = "gt-normal" 
#     time.sleep(0.5)
#     os.system("clear")
#     #roots input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "roots":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Roots: "))
#     if op == 1:
#         roots = "Desconhecido"
#     elif op == 2:
#         roots = "Norm"
#     elif op == 3:
#         roots = "Rotted"
#     elif op == 4:
#         roots = "galls-cysts" 
#     time.sleep(0.5)
#     os.system("clear")
#     #sclerotia input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "sclerotia":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Sclerotia: "))
#     if op == 1:
#         sclerotia = "Desconhecido"
#     elif op == 2:
#         sclerotia = "Absent"
#     elif op == 3:
#         sclerotia = "Present"
#     time.sleep(0.5)
#     os.system("clear")
#     #seed input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "seed":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Seed: "))
#     if op == 1:
#         seeds = "Desconhecido"
#     elif op == 2:
#         seeds = "Norm"
#     elif op == 3:
#         seeds = "Abnorm"
#     time.sleep(0.5)
#     os.system("clear")
#     #seed-discolor input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "seed-discolor":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Seed Discolor: "))
#     if op == 1:
#         seedDiscolor = "Desconhecido"
#     elif op == 2:
#         seedDiscolor = "Absent"
#     elif op == 3:
#         seedDiscolor = "Present" 
#     time.sleep(0.5)
#     os.system("clear")
#     #seed-size input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "seed-size":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Seed Size: "))
#     if op == 1:
#         seedSize = "Desconhecido"
#     elif op == 2:
#         seedSize = "Norm"
#     elif op == 3:
#         seedSize = "lt-norm" 
#     time.sleep(0.5)
#     os.system("clear")
#     #seed_tmt input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "seed-tmt":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Seed Tmt: "))
#     if op == 1:
#         seedTmt = "Desconhecido"
#     elif op == 2:
#         seedTmt = "none"
#     elif op == 3:
#         seedTmt = "fungicida"
#     elif op == 4:
#         seedTmt = "Outros"  
#     time.sleep(0.5)
#     os.system("clear")
#     #severity input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "severity":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Severity: "))
#     if op == 1:
#         severity = "Desconhecido"
#     elif op == 2:
#         severity = "Minor"
#     elif op == 3:
#         severity = "pot-severe"
#     elif op == 4:
#         severity = "severe"   
#     time.sleep(0.5)
#     os.system("clear")
#     #shriveling input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "shriveling":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Shriveling: "))
#     if op == 1:
#         shriveling = "Desconhecido"
#     elif op == 2:
#         shriveling = "Absent"
#     elif op == 3:
#         shriveling = "Present"
#     time.sleep(0.5)
#     os.system("clear")
#     #stem input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "stem":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Canker Lesion: "))
#     if op == 1:
#         stem = "Desconhecido"
#     elif op == 2:
#         stem = "Norm"
#     elif op == 3:
#         stem = "Abnorm"
#     time.sleep(0.5)
#     os.system("clear")
#     #stem-cankers  input 
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "steam-cankers":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Steam Cankers: "))
#     if op == 1:
#         steamCankers = "Desconhecido"
#     elif op == 2:
#         steamCankers = "Absent"
#     elif op == 3:
#         steamCankers = "below-sool"
#     elif op == 4:
#         steamCankers = "Above-soil"
#     elif op == 5:
#         steamCankers = "Above-sec-nde"    
#     time.sleep(0.5)
#     os.system("clear")
#     #temp input
#     aux = 1
#     for i in atributos:
#         if atributos[i][0] == "temp":
#             print(aux," - ",atributos[i][2])
#             aux+=1
#     op = int(input("Temp: "))
#     if op == 1:
#         temp = "Desconhecido"
#     elif op == 2:
#         temp = "lt-norm"
#     elif op == 3:
#         temp = "norm"
#     elif op == 4:
#         temp = "gt-norm" 
#     time.sleep(0.5)
#     os.system("clear")
