maxgissningar = 6
space = ("\n") * 100
liv = 0
blankspaceahh = True
gissningar = 0
wincon = False

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

while liv < maxgissningar and wincon == False:
     stavcon = False
     giss = str(input("gissa bokstäverna \n"))
     current_pos = int(0)
     for letter in ordet:
          if giss == letter:
               stavcon = True
               word_progress[current_pos] = giss
               print("du gissade rätt \n")
               print(word_progress)
          current_pos += 1


               
               
     if stavcon == False:
          liv = liv + 1
          print("Du gissade fel", lifeline[liv])
          print(word_progress)

     
     if "".join(word_progress) == "".join(ordet):
          wincon = True

if wincon == True:
     print("Yippie!")
     print(f'Ordet var {"".join(ordet)}')



if liv == maxgissningar:
     print("Du förlorade spelet")


