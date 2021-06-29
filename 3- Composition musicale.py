entree = list(input())
nbNotes = len(entree)
nbDoublons = -1

while nbDoublons != 0:
   nbDoublons = 0
   x = 0
   y = 0
   while x < nbNotes :
      if (x < nbNotes - 1) and (entree[x] == entree[x+1]):
         x += 2
         nbDoublons += 1
      else:
         entree[y] = entree[x]
         x += 1
         y += 1
   nbNotes = nbNotes - 2 * nbDoublons
pos = 0
for loop in range(nbNotes):
   print(entree[pos], end = '')
   pos += 1