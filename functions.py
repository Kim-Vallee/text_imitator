#!/usr/bin/python3.4
# coding: utf8
import sys
import random
"""File where all the functions are stocked"""
def notre_text(answer):
    """ Function testing user's answer"""
    texte1 = str()
    if answer.lower() == 'y':
        texte1 = "The stacked magazines were seriously worn. The piles weren't\
         neat, didn't seem to be arranged by year or subject matter. They weren't\
         bound together, fastened to anything or stored in containers, which meant\
         sudden stops were potentially life-threatening. The cab was also full of\
         smoke, which I attributed to spontaneous mildew combustion, or a dropped\
         cigarette or ashtray overflow which resulted in a slow burn through slick\
         paper. Maybe the guy was deeply involved in bizarre barbecue hara-kiri \
         peep-show suicide."
    elif answer.lower() == 'n':
        print('Veuillez entrer un texte de 1000 charactères ou plus : ')
        texte1 = str(sys.stdin.read(1000)) # sys.stdin.read()
                                        # permet de copier tout                                        # un texte.
    else:
        notre_text(str(input('Veuillez répondre par y/n : ')))
    return str(texte1)

def supprime_accent(texte):
    """ supprime les accents du texte source """
    texte = texte.lower()
    accent = ['é', 'è', 'ê', 'à', 'ù', 'û', 'ü', 'ç', 'ô', 'ö', 'î', 'ï', 'â', 'ß']
    sans_accent = ['e', 'e', 'e', 'a', 'u', 'u', 'u', 'c', 'o', 'o', 'i', 'i', 'a', 'ss']
    i = 0
    while i < len(accent):
        texte = texte.replace(accent[i], sans_accent[i])
        i += 1
    texte = texte.replace("'",' ')
    return texte

def get_after_letter(indices, temp_list, liste_text, i):
    """Fuction getting each letter after another"""
    j = 0
    # On fait tourner jusqu'à ce qu'il n'y ait plus de correspondance avec cette lettre
    # Voir l.23
    while j < len(indices[i]):
        # Try / except pour éviter les erreurs de dernier charactère
        try:
        # On stock les lettres suivants la lettre alphabet[i] dans temp_list
            if (liste_text[indices[i][j] + 1] != ',' and liste_text[indices[i][j] + 1] != '.'):
                temp_list.append(liste_text[indices[i][j] + 1])
        except IndexError:
            pass
        j += 1
    return temp_list

# def get_temp_list_chance(alphabet, temp_list):
#     """ Updating temp list chance"""
#     temp_last = 0
#     temp_list_chance = list()
#     g = 0
#     while g < len(alphabet):
#         if (temp_list.count(alphabet[g])) != 0: # On évite les zéros inutiles
#             # Try catch pour éviter la division par zero
#             try:
#                 # On compte le nombre de fois qu'il y a de lettre alphabet[g] après
#                 # la lettre alphabet[i] et on le met en pourcentage
#                 percent = round((temp_list.count(alphabet[g])/len(temp_list))*100)
#                 # Pour éviter d'avoir un pourcentage supérieur à zero à cause des
#                 # arrondis
#                 if((percent + temp_last) > 100):
#                     percent = 100
#                     temp_last = 0
#                 # On ajoute à une liste temporaire un tuple (ici sous forme de liste)
#                 # qui servira à completer un dico
#                 temp_list_chance.append([alphabet[g],percent + temp_last])
#                 # Pour des raisons de facilité d'aléatoire, la probabilité vaut
#                 # la probabilité originiel + les probabilités précédentes
#                 temp_last += percent
#             except ZeroDivisionError:
#                 pass
#         g += 1
#     try:
#         if temp_list_chance[-1][1] != 100:
#             temp_list_chance[-1][1] = 100
#     except IndexError:
#         pass
#     return temp_list_chance

def get_chance_of_first_letter(alphabet, amount_of_word, splitted_txt):
    """ Getting the chance of a first letter of a word """
    chance_of_first_letter = list()
    i = 0
    temp_list = [] # reset
    while i < amount_of_word:
        temp_list.append(splitted_txt[i][0])
        i += 1

    i = 0
    temp_last = 0
    while i < len(alphabet):
        if temp_list.count(alphabet[i]) != 0:
            chance_of_first_letter.append([alphabet[i], (temp_list.count(alphabet[i])\
            /amount_of_word)*100 + temp_last])
            temp_last += temp_list.count(alphabet[i])/amount_of_word*100
        i += 1
    chance_of_first_letter[-1][1] = 100
    return chance_of_first_letter

def doubling_letter(amount_of_word, splitted_txt, alphabet,indices):
    """Getting a chance of to letter to be followed in a word like tt"""
    i = 0
    temp_list = []
    doubling_letter_chance = dict()
    while i < amount_of_word:# First going throught the splitted text
        j = 0
        while j < len(splitted_txt[i]):
            if j != 0:
                if splitted_txt[i][j] == splitted_txt[i][j-1]:
                    temp_list.append(splitted_txt[i][j])
            j += 1
        i += 1

    i = 0
    while i < len(alphabet):
        if alphabet[i] in temp_list:
            doubling_letter_chance[alphabet[i]] = round(temp_list.count(alphabet[i])/len(indices[i])*100)
        i += 1
    return doubling_letter_chance
