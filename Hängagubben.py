maxgissningar = 5
space = ("\n") * 100
liv = -1
stavcon = False
blankspaceahh = True
gissningar = 0

lifeline = [
r"""
 ♥ ♥ ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥ ♥
      O
     /|\
     / \
""",
r"""
 ♥
      O
     /|\
     / \
""",
r"""
      
      O
     /|\
     / \
"""
]

startgame = str(input("Vill du spela hängagubbe? y för ja och n för nej. \n")) 

if startgame == "y":
    ordet = str(input("Skriv in ett ord som din motståndare ska gissa, din motståndare får 6 gissningar\n"))
elif startgame == "n":
    print("Bye Bye lil bro")
else:
    print("Fuck you då")

word_progress = list("_" * len(ordet))
ordet = list(ordet)
print(ordet)
print(space)
print("Ordet är", len(ordet), "Bokstäver långt ")
current_pos = int(0)

while liv < maxgissningar:
    giss = str(input("gissa bokstäverna \n"))
    for letter in ordet:
          if giss == letter:
            gissningar = gissningar + 1
            stavcon = True
            word_progress[current_pos] = giss
            print("du gissade rätt \n")
            print(word_progress)
            current_pos += 1
               
               
          if stavcon == False:
               liv = liv + 1
               print("Du gissade fel", lifeline[liv])
               print(word_progress)



if liv == maxgissningar:
     print("Du förlorade spelet")






















                  
