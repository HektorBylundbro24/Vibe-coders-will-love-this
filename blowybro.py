#uppgift 1 classroom Moa docs

#hälsning = "Hejsan svejsan"

#namn = "Hektor"

#längd = "1.84m"

#favnummer = "12"

#print(hälsning, " jag heter " + namn + " jag är " + längd + " lång och mitt favorit nummer är " + favnummer)

##############################################

#uppgift 3 classroom moa docs

#nummer = input("Skriv ett nummer: ")

#dubbelnummer = float(nummer) * 2

#print("Ditt nummer är: ", nummer, " och det dubbla är: ", f"{dubbelnummer:.3f}")

#############################################

#uppgift 4 classroom moa docs

#ålder = input("Hur gammal är du?")

#femårålder = int(ålder) + 5

#print("Idag är du", ålder, "gammal", " och om fem år är du", femårålder, "gammal")

############################################

#uppgift 7 classroom Moa docs

#bredd = input("Hur långt är ditt rum?")

#längd = input("Hur breddt är ditt rum?")

#area = int(bredd) * int(längd)

#print("Ditt rum är", area, "kvadratmeter stort")

############################################

#uppgift 10 classroom Moa docs

#pris = input("Vad kostar varan")

#rea = input("Vad är rean")

#rea2 = int(pris) / 100 * int(rea)

#slutpris = int(pris) - int(rea2)

#print("Rabbaten är", rea2)

#print("Det slutgiltiga priset är", slutpris)

###########################################

#uppgift 11 classroom Moa docs

#biljett = int(input("Hur många biljetter ska ni ha?"))

#pris = biljett * 120

#pris2 = biljett * 75

#slutpris = int(pris) + int(pris2)

#print("Biljetterna kostar tillsammans", pris, "kr")

#print("Läsk och popcorn kostar tillsammans", pris2, "kr")

#print("Tillsammans kostar biljetter och snacks", slutpris, "kr")

###########################################

#uppgift 12 classroom Moa docs

#import math

#radie = int(input("Vad är cirkelns radie?"))

#diametern = int(input("Vad är cirkelns diameter?"))

#omkrets = diametern * math.pi

#area = radie * 2 * math.pi

#print("Cirkelns omkrets är", omkrets, " cm")

#print("Cirkelns area är", area, " cm")

###########################################

#uppgift 13 classroom Moa docs

#import math

#radie = int(input("Vad är pizzans radie i kvadrat centimeter?"))

#area = radie * math.pi

#print("Pizzans area är", area, "cm2")

###########################################

#uppgift 14 classroom Moa docs

#import math

#cirkelr1 = int(input("Vad är cirkel1s radie?"))

#cirkelr2 = int(input("Vad är cirkel2s radie?"))

#cirkelarea1 = cirkelr1 * math.pi

#cirkelarea2 = cirkelr2 * math.pi

#skillnadenarea = cirkelarea1 - cirkelarea2 if cirkelarea1 > cirkelarea2 else cirkelarea2 - cirkelarea1

#print("Cirkel1s area är", cirkelarea1)
#print("Cirkel2s area är", cirkelarea2)
#print("Skillnaden mellan cirklarnas area är", skillnadenarea)

###########################################

#uppgift 15 classroom Moa docs

#import random



#x = random.randint(1, 6)


###########################################

#uppgifter kapitel 3 3.0

#grader = float(input("Hur varmt är det?"))

#if(grader > 0):
#    print("Det är plusgrader!")
#else: 
#    print("Det är minusgrader")

###########################################

#uppgifter kapitel 3 6.0

#lösenord = (input("Vad är lösenordet"))

#lösen = ("arvidblow24")

#if(lösenord == lösen):
#    print("Lösenordet är korrekt")
#else:
#    print("Det är fel lösenord, försök igen")

##########################################

#uppgift kapitle 3 7.0

celsius = int(input("Hur varmt är det?"))

if (celsius >= 0 and celsius <= 9):
    print("Det är cold")
elif(celsius >= 10 and celsius <= 19):
    print("Det är inte så cold")
elif(celsius < 0):
    print("Det var ICECOLD!")
elif(celsius > 19):
    print("Det var crazy HOT!")