#1.1.1
annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]
print("Liste de base : ")
print(annee)
annee.pop()
annee.pop()
annee.pop()
print("#1.1.1 : ")
print(annee)


#1.1.2
annee.insert(len(annee),"Octobre")
annee.insert(len(annee),"Novembre")
annee.insert(len(annee),"Decembre")
print("#1.1.2 : ")
print(annee)


#1.1.3
annee[9] = "Octobre"
annee[10] = "Novembre"
annee[11] = "Decembre"
print("#1.1.3 : ")
print(annee)


#1.1.4
x = [1, 2, 3, 4, 3, 5, 3, 1, 3, 2]
resultat = [y+1 for y in x]
print("#1.1.4 : ")
print(resultat)


