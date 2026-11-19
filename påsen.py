påsen = []
påsenquantum = []
påse_loop = True

while påse_loop == True:
    print("Welcome to THE påse!")
    print("-" * 40)
    print("[V] Visa innehållet i påsen \n[S] Spara i påsen \n[F] Leta (finns) i påsen \n[Q] Avsluta programmet \n[B] Ta bort från påsen \n")
    val = input("Välj vad du vill göra ").upper()
    if val == "V":
        if len(påsen) == 0:
            påse_loop = False
            print("Din påse är tom")
            fortsätt = input("Vill du fortsätta? Skriv Y \n").upper()
            if fortsätt == "Y":
                påse_loop = True
            else:
                break

        else:
            påse_loop = False
            print(påsen)
            fortsätt2 = input("Vill du fortsätta? Skriv Y \n").upper()
            if fortsätt2 == "Y":
                påse_loop = True
            else:
                break

    elif val == "S":
        påse_loop = False
        påsen.append(input("Vad vill du lägga till i påsen? "))
        fortsätt3 = input("Vill du fortsätta? Skriv Y \n").upper()
        if fortsätt3 == "Y":
            påse_loop = True
        else:
            break

    elif val == "F":
        påse_loop = False
        leta = input("Vad vill du leta efter ")
        for word in påsen:
            if leta == word:
                print(f"Du hittade {leta}!")
            else:
                print(f"Du hittade inte {leta}")
        fortsätt4 = input("Vill du fortsätta? Skriv Y \n").upper()
        if fortsätt4 == "Y":
            påse_loop = True
        else:
            break

    elif val == "Q":
        print("Well fuck you då!")
        break

    elif val == "B":
        påsenbort = input("Vad vill du ta bort")
        påsen.remove(påsenbort)





    else:
        pass