nbreValeurs = int(input())
seuil = float(input())
valeurs = [float(input()) for loop in range(nbreValeurs)]
temp = [0.0] * nbreValeurs

def lisse():
   for valeur in range(1, nbreValeurs):
      if abs(valeurs[valeur] - valeurs[valeur -1]) > seuil:
         return False
   return True
   
nbreTours = 0
while not lisse():
   nbreTours = nbreTours + 1
   for valeur in range(1, nbreValeurs - 1):
      temp[valeur] = (valeurs[valeur - 1] + valeurs[valeur + 1]) / 2
   for valeur in range(1, nbreValeurs - 1):
      valeurs[valeur] = temp[valeur]
      
print(nbreTours)