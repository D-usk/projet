
mots_fr = []
mots_cherches = []


dicofr = open("dicofr.txt", "r")
liste_mots_fr = dicofr.readlines()
for i in liste_mots_fr:
    i.lower()
    mots_fr.append(i.replace("\n", ""))


def recherche(dico):
    start = input("Premiere lettre du mot: ")
    longueur = input("Longueur du mot: ")
    lettres = input("lettres dans le(s) mot(s): ")

    for index in dico:
        if index[0] == start and len(index) == int(longueur) and lettres in index:
            mots_cherches.append(index)
        if start == "" and len(index) == int(longueur) and lettres in index:
            mots_cherches.append(index)




recherche(mots_fr)
print(mots_cherches)
