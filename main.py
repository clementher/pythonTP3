#1.1.1
annee = ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre',10,11,12]
print("Liste Partie 1 : ")
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
print(" ")

#2.1
moisDeLannee = ('Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre')
print("Liste Partie 2 : ")
print(moisDeLannee)
print("#2.1 : ")
print(moisDeLannee[3])


#2.2
print("#2.2 : ")
print('"Mars" in moisDeLannee')
print("Mars" in moisDeLannee)
print(" ")


#3.1
age = {"pierre" : 35 , "paul" : 32 , "Jacques" : 27 , "andre" : 23}
print("Liste Partie 3 : ")
print(age)
age.update({"david" : 22 , "veronique" : 21 , "sylvie" : 30 , "damien" : 37})
print("#3.1 : ")
print(age)


#3.2
print("#3.2 : ")
print(age['sylvie'])


#3.3
someone = "andre"
print("#3.3 : ")
if someone in age:
  print(someone + " is PRESENT")
else:
  print(someone + " is ABSENT")


#3.4
club = ({
  "pierre durand":(1986, 1.72, 70),
  "victor dupont":(1987, 1.89, 57),
  "paul dupuis":(1989, 1.60, 92),
  "jean rieux":(1985, 1.88, 77)
})

data = ({'c':3,'d':4})  
print("#3.4 : ")



