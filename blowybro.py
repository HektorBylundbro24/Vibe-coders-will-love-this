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

#uppgift kapitel 3 7.0

#celsius = int(input("Hur varmt är det?"))

#if (celsius >= 0 and celsius <= 9):
#    print("Det är cold")
#elif(celsius >= 10 and celsius <= 19):
#    print("Det är inte så cold")
#elif(celsius < 0):
#    print("Det var ICECOLD!")
#elif(celsius > 19):
#    print("Det var crazy HOT!")

##########################################

#uppgift kaptiel 3 8.0

#poäng = int(input("Hur många poäng fick du"))

#if(poäng <= 50):
#    print("Du har F")
#elif(poäng >= 50 and poäng <= 59):
#    print("Du har E")
#elif(poäng >= 60 and poäng <= 69):
#    print("Du har D")
#elif(poäng >= 70 and poäng <= 79):
#    print("Du har C")
#elif(poäng >= 80 and poäng <= 89):
#    print("Du har B")
#elif(poäng >= 90 and poäng <= 100):
#    print("Du har A du är crazy cold")

#########################################

#uppgift kapitel 3 13.0

#räknesätt = (input("Vilket räknesätt vill du använda?, + - / *"))
#tal1 = int(input("Skriv ett tal"))
#tal2 = int(input("Skeiv ännu ett tal"))

#minus = "-"
#plus = "+"
#ggr = "*"
#division = "/"

#tal3 = tal1 + tal2
#tal4 = tal1 - tal2 if tal1 > tal2 else tal2 - tal1
#tal5 = tal1 * tal2
#tal6 = tal1 / tal2

#if(räknesätt == plus):
#    print("Det är likamed", tal3)
#elif(räknesätt == minus):
#    print("Det är likamed", tal4)
#elif(räknesätt == ggr):
#    print("Det är likamed", tal5)
#elif(räknesätt == division):
#    print("Det är likamed", tal6)
#lse:
#    print("Skriv in ett räknesätt för att använda miniräknaren")

##########################################

#Uppgift kapitel 3 14.0

#import random

#randonummer = random.randint(1,10)

#försök = 3

#while försök > 0:
#    försök = försök - 1
#    Gissning = int(input("Säg ett tal från 1 - 10\n"))
#    if randonummer == Gissning:
#        print("Du gissade rätt!")
#    elif Gissning > randonummer:
#       print("Din gissning är för hög")
#    elif Gissning < randonummer:
#        print("Din gissning är för låg")
    
#############################################

#uppgift kapitel 3 15.0

#Inge int Moa bro

#############################################

#uppgift kapitel 4 1.0

#heltal = int(input("Skriv ett heltal"))

#talet = 0

#while talet < heltal:
#    talet = talet + 1
#    print([talet])

############################################

#uppgift kapitel 4 9.0

#heltal = int(input("Skriv ett heltal "))

#talet = 0

#while talet < heltal:
#    talet = talet + 1
#    if talet % 3 == 0:
#        continue
#    else:
#        print([talet])

############################################

#uppgift 5.1 kapitel 5

#print("Du har en \u265a och \u03C0")

############################################

#uppgift 5.2 kapitel 5

#text = input("Skriv din favorite deadlock dialouge \n")

#if text[0] == text[-1]:
#    print("Dem är samma")
#else:
#    print("Du är dum")

############################################

#uppgift 5.3 kapitel 5

#v = "pytonorm"

#v[1:3]

#print(v[1:3:5])

############################################

#uppgift 5.4 kapitel 5

#s = input("Skriv en text pretty please \n")
#s2 = s[::-1]
#i = 0

#for c in s2:
#    if c == " " or c == "\t":
#        break
#    i = i + 1
#if i < len(s2):
#    print(f"första vita tecknet finns på plats nr {i}")
#else:
#    print("Ingen vitt bokstav")

###########################################

#uppgift 5.4 kapitel 5

ord = input("ord")
len(ord)
print(len(ord))