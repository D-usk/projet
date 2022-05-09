liste_mots_fr = []

with open("dicofr.txt", "r") as line:
    for mot in line:
        liste_mots_fr.append(mot.lower().replace("\n",""))

def recherche_positions(lettres, liste_mots_fr):
    liste_valide = []
    total_lettres = len(lettres.keys())
    for mot in liste_mots_fr:
        current_count = 0
        for key, value in lettres.items():
            lettres_mot = { i:mot[i] for i in range(0,len(mot)-1) }
            if lettres_mot.get(int(key)) == value:
                current_count += 1

        if current_count == total_lettres:
            liste_valide.append(mot)
    return liste_valide


def taille_mot():


print("Si vous connaissez une/plusieurs positions des lettres , veuillez les inscrires sous le format position:lettre (ex 0:a pour assez")
prem_lettres = input("lettre du mot: ")
positions_lettre_connues = {}

while prem_lettres != "ok":
    prem_lettres = prem_lettres.split(":")
    if(prem_lettres is not None):
        positions_lettre_connues[prem_lettres[0]] = prem_lettres[1]
    prem_lettres = input("lettre du mot: ")

##longueur = int(input("Longueur du mot: "))
liste_valide_offset = recherche_positions(positions_lettre_connues, liste_mots_fr)
print(liste_valide_offset)
"""""
for index in dico:
    if index[0] == start and len(index) == longueur and lettres in index:
        mots_cherches.append(index)
    if start == "" and len(index) == longueur and lettres in index:
        mots_cherches.append(index)
    if index[0] == start and longueur == "" and lettres in index:
        mots_cherches.append(index)
    if index[0] == start and len(index) == longueur and lettres in index:
"""
##print(mots_cherches)
