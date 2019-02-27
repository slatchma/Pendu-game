#! /usr/bin/env python
# -*-coding:Utf-8 -*

#-------------------------
#MAIN
#-------------------------
#import
import time
import os
import function

#Initialisation
choice = 0
error = 0

error = function.ft_error()
while error == 0:
    print('--- JEU DU PENDU ---')
    print('---------- MENU ----------')
    print('Veuillez choisir le mode')
    print('1 joueur : tapez 1')
    print('2 joueurs : tapez 2')
    print('Sortie : tapez q')
    choice = input('choix ?\n')
    if choice == 'q':
        print('AUREVOIR')
        break
    if choice != '1' and choice != '2':
        os.system('clear')
        print('Veuillez rentrer une bonne valeur\n')
        continue
    if choice == '1':
        os.system("clear") #clean de la console
        print('--- PENDU 1 joueur ---')
        function.ft_gamer_one()
        os.system('clear')
    elif choice == '2':
        os.system('clear')
        print('--- PENDU 2 joueurs ---')
        function.ft_gamer_two()
        os.system('clear')     