nbLettres = int(input())
lettre = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
taille = 2*nbLettres - 1

iLig = 0
for loop in range(taille):
   iCol = 0
   for loop in range(taille):
      print(lettre[min(min(iLig,taille-1-iLig), min(iCol, taille-1-iCol))], end = "")
      iCol = iCol + 1
   iLig = iLig + 1
   print("")