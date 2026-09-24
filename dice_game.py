import random

start = input("Vill du spela blackjack?, y för att starta, n för att avsluta: ")

poängsumma = 0

rullningar = 0
rullerblow = True

if start == "y":
    print("Kom så nära 21 utan att gå över")
    while rullerblow == True:
        nummertärning = random.randint(1, 6)
        poängsumma = nummertärning + poängsumma
        if rullningar == 0:
            print(nummertärning)
        elif rullningar >= 1:
            print(nummertärning, "\nDin totala summa är: ", poängsumma)

        if poängsumma > 21:
            rullerblow = False
            start2 = input("Du fick över 21 och förlorade, vill du spela igen?, y eller n: ")
            if start2 == "y":
                rullerblow = True
                poängsumma = poängsumma - poängsumma 
                rullningar = rullningar - rullningar
            elif start2 == "n":
                print("ByeByelilbro")
                break

        elif poängsumma == 21:
            start2 = input("Du fick 21! Vill du spela igen? y eller n: ")
            if start2 == "n":
                print("Fegis bro")
                rullerblow = False
                break
            elif start2 == "y":
                poängsumma = poängsumma - poängsumma 
                rullningar = rullningar - rullningar


        rullaigen = input("Vill du rulla igen?, y eller n: ")
        if rullaigen == "y":
            rullningar = rullningar + 1
        elif rullaigen == "n":
            rullerblow = False
            print("Din jävla fegis")
        else:
            rullerblow = False
            print("Snälla svara y eller n")

                
else:
    print("byebye (reverb + slowed)")

