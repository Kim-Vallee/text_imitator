#!/usr/bin/python3.4
# coding: utf8
"""Main file to run"""
# On importe toute les données nécessaires
from datas import *
from functions import *
from classes import *
import sys
import random

texte = notre_text(str(input('Voulez vous utiliser un de nos texte ? [y/n] : ')))
texte = supprime_accent(texte) # On supprime les accents
longueur_texte = len(texte) # On récupère la longueur du texte

for ltrs in texte: # On transforme tout le texte en liste
    liste_text.append(ltrs)

# On récupère les chances d'avoir une lettre après une autre
i = 0
while i < len(alphabet): # On parcours tout l'alphabet
    # On regarde où se situent les différents index de la lettre
    indices.append([j for j, x in enumerate(liste_text) if x == alphabet[i]])
    # On reset les variables temporaires
    temp_list = []
    temp_list_chance = []
    temp_last = 0

    temp_list = get_after_letter(indices, temp_list, liste_text, i)
    # temp_list_chance = get_temp_list_chance(alphabet, temp_list)

    # On ajoute la liste temp_list_chance au dico qui vaut
    # letter: [[following letter, percent][another following letter,another percent]]
    if temp_list != []:
        chance_after_letter[alphabet[i]] = temp_list
    i += 1
splitted_txt = texte.split()
amount_of_word = len(splitted_txt)


chce_frst_ltr = get_chance_of_first_letter(alphabet, amount_of_word, splitted_txt)

doubling_letter_chance = doubling_letter(amount_of_word, splitted_txt, alphabet,indices)

# Getting shortest and longest word of the text + making mid-size:
mid_size = int()
i = 0
while i < len(splitted_txt):
    if i == 0:
        shortest_word = len(splitted_txt[i])
        longest_word = len(splitted_txt[i])
    elif shortest_word > len(splitted_txt[i]):
        shortest_word = len(splitted_txt[i])
    elif longest_word < len(splitted_txt[i]):
        longest_word = len(splitted_txt[i])
    mid_size += len(splitted_txt)
    i += 1
mid_size = mid_size / len(splitted_txt)
list_shortests = list()
list_longests = list()
i = 0
while i < len(splitted_txt):
    if len(splitted_txt[i]) == shortest_word:
        list_shortests.append(splitted_txt[i])
    elif len(splitted_txt[i]) == longest_word:
        list_longests.append(splitted_txt[i])

    i += 1
new_text_length = int(input('Veuillez entrer la taille du texte que vous voulez créer : '))
texte_created = str()
i = 0
while i < new_text_length:
    random_1 = random.randrange(100)
    word = NewWord(shortest_word, longest_word, random_1, chce_frst_ltr, mid_size)
    new_word = word.create_word(chance_after_letter, chce_frst_ltr, doubling_letter_chance, shortest_word, longest_word, list_longests, list_shortests)
    if ' ' in new_word:
        texte_created += new_word
    else:
        texte_created += new_word + ' '
    i += 1
texte_created += '.'
i = 6
# while i > 1:
#     space = ' '
#     texte_created = texte_created.replace(space * i, ' ')
#     i -= 1
print(texte_created)
