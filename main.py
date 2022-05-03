"""
Retourne le dictionnaire des animaux 
"a": ["animal"],
... 
"""
import listAdjectifs
import listAnimals

import unicodedata
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def populate_dict(une_liste):
    dic_ = {}
    for element in une_liste:
        e = strip_accents(element[0].lower())
        if e not in dic_:
            dic_[e] = []
        dic_[e].append(element.lower())
    return dic_

def find_entry(name, dict):
    index = find_hashed_index(name, dict)
    stripped = strip_accents(name.lower()[0])
    return dict[stripped][index]

def find_hashed_index(name, dict):
    big_number = 0
    for c in name.lower():
        stripped = strip_accents(c.lower())
        big_number += ord(stripped)
    big_number = big_number % len(dict[stripped]) - 1
    return big_number


def main():
    dict_animals = populate_dict(listAnimals.animals)
    dict_adjectives = populate_dict(listAdjectifs.adjectives)

    prenoms = ["Emmannuel", "Elliott", "Etta", "Ergaud"]

    noms = ["Excellent", "Bideau", "Zwörgen", "Mineau"]

    for prenom in prenoms:
        print(find_entry(prenom, dict_animals))

    for nom in noms:
        print(find_entry(noms, dict_adjectives))

if __name__ == "__main__":
    main()