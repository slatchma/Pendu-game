#import
import time
import os


#-------------------------
#Partie du jeu où on essaye de deviner le mot
#-------------------------
def ft_pendu(j, word):
    #Initialisation
    essay = 7
    word_ghost = []
    letter = ''

    word = word.lower()
    word_ghost = list(word)
    for i in range(0, len(word_ghost)):
        word_ghost[i] = '_'

    while essay >= 0:
        print('\n', ' '.join(word_ghost))
        print('essai = ', essay)
        while True:
            print(j['name'], 'c\'est à vous, entrez une lettre')
            letter = input()
            if len(letter) != 1 or letter.isalpha() != True:
                print('Erreur, entrez une lettre')
            else:
                break
        if (letter in word):
            for i in range(0, len(word_ghost)):
                if word[i] == letter:
                    word_ghost[i] = letter
        else:
            print('pas de lettre <<', letter, '>> dans le mot')
            essay += -1
        if not('_' in word_ghost):
            print('le mot était <<', word, '>>')
            print('\nBRAVO', j['name'], 'Vous avez gagnez')
            time.sleep(3) #pause de 1 seconde
            os.system('clear')
            return 1

    print('le mot était <<', word, '>>')    
    print('\nDOMMAGE', j['name'], 'Vous avez perdu')
    time.sleep(3)
    os.system('clear')
    return -1


#-------------------------
#Partie 2 joueurs suite : on regarde si le mot mis par le joueur est bon.
# Si tout est ok on lance le pendu
#-------------------------
def ft_game(j1, j2):
    #Initialisation
    word = ''

    while True:
        print(j1['name'], 'entrez un mot')
        word = input()
        if (word.isalpha() == False):
            print('mot non valide')
        else:
            break
    os.system('clear')
    return ft_pendu(j2, word)
    

#-------------------------
#partie 1 joueur
# On utilise le fichier word pour charger les mots
#-------------------------
def ft_gamer_one():
    #import
    from random import randint #Pour choisir un nbre au hasard
    
    #Initialisation
    j1 = {'name': 'j1', 'pts': 0}
    tour = 1
    word = ''
    my_file = open('word', 'r')
    word_list = my_file.read()
    word_list = word_list.split('\n')
    my_file.close

    print('REGLES\n')
    print('Le joueur doit deviner le mot caché. Il a 7 essais pour trouver le mot')
    print('Si le joueur1 marque 2 points en 3 manches max, il gagne la partie\n')
    j1['name'] = input('joueur1, quel est votre nom ?\n')
    j1['name'] = j1['name'].upper()
    print('joueur1 vous vous appelez <<', j1['name'], '>>\n')
    while j1['pts'] < 2 and tour < 4:
        print('Points\t', j1['name'], '=', j1['pts'])
        time.sleep(1)
        word = word_list[randint(0, len(word_list))]
        print('Manche ', tour)
        if ft_pendu(j1, word) == 1:
            j1['pts'] += 1
        tour += 1

    print('FINI !!!')
    print('Points\n', j1['name'], '=', j1['pts'])
    if j1['pts'] == 2:
        print('BRAVO !!!', j1['name'], 'Vous avez gagnez !!!')
    else:
        print('DOMMAGE !!!', j1['name'], 'Vous avez perdu !!!')
    time.sleep(7) #pause de 1 seconde        


#-------------------------
#Partie 2 joueurs
#-------------------------
def ft_gamer_two():
    #Initialisation
    j1 = {'name': 'j1', 'pts': 0}
    j2 = {'name': 'j2', 'pts': 0}
    tour = 1

    print('REGLES\n')
    print('Les joueurs doivent deviner le mot caché. Ils ont 7 essais pour trouver le mot')
    print('Le 1er qui marque 2 points, gagne la partie\n')
    j1['name'] = input('joueur1, quel est votre nom ?\n')
    j1['name'] = j1['name'].upper()
    print('joueur1 vous vous appelez <<', j1['name'], '>>\n')
    j2['name'] = input('joueur2, quel est votre nom ?\n')
    j2['name'] = j2['name'].upper()
    print('joueur2 vous vous appelez <<', j2['name'], '>>\n')

    while j1['pts'] < 2 and j2['pts'] < 2:
        print('Points\n', j1['name'], '=', j1['pts'], '\t', j2['name'], '=', j2['pts'])
        time.sleep(1) #pause de 1 seconde        
        if (tour % 2) == 1:
            print('Manche ', tour)
            if ft_game(j1, j2) == 1:
                j2['pts'] += 1
            else:
                j1['pts'] += 1
        else:
            if ft_game(j2, j1) == 1:
                j1['pts'] += 1
            else:
                j2['pts'] += 1  
        tour += 1

    print('FINI !!!')
    print('Points\n', j1['name'], '=', j1['pts'], '\t', j2['name'], '=', j2['pts'])
    if (j1['pts'] > j2['pts']):
        print('BRAVO !!!', j1['name'], 'Vous avez gagnez !!!')
    else:
        print('BRAVO !!!', j2['name'], 'Vous avez gagnez !!!')
    time.sleep(7) #pause de 1 seconde        


#-------------------------
#On regarde si le fichier word est valide, sans ça, le jeu ne se lance pas
#-------------------------

def ft_error():
    try:
        my_file = open('word', 'r')
    except:
        print('error : word file not exist')
        return 1
    word_list = my_file.read()
    if len(word_list) == 0:
        print('error : in the world file, file empty')
        return 1
    word_list = word_list.split('\n')
    my_file.close 
    for i in range(0, len(word_list)):
        if word_list[i].isalpha() == False:
            print('error : in the word file, line', i + 1, 'not word')
            return 1  
    return 0