nbLivres, nbJours = map(int, input().split())
tempsRestantLivre = [0]*nbLivres
idLivre = 0

# idLivre initialisé à 0 dans notre tableau tempsRestantLivre 
for loop in range(nbLivres):
   tempsRestantLivre[idLivre] = 0
   idLivre+=1

   
for loop in range(nbJours):
   nbClients = int(input()) # nombre de clients par jour
   for loop in range(nbClients):
      livre, temps = map(int, input().split()) # pour chaque client on récupère id et durée
      if (tempsRestantLivre[livre] <= 0): 
         tempsRestantLivre[livre] = temps
         print(1)
      else:
         print(0)
   idLivre = 0
   for loop in range(nbLivres): 
      tempsRestantLivre[idLivre] -= 1 # chaque jour écoulé on décrémente de 1 sur notre temps restant pour chaque livre
      idLivre+=1 # on incrémente notre id de 1 à chaque boucle