import random 
import string
from mots import mots

vies = 6
mot = random.choice(mots).upper()
lettre_mot = set(mot)
alphabet = set(string.ascii_uppercase)
used_letters = set()

pendu_images = [ "DEEAD",
    '''
    +---+
    |   |
    O   |
   /|\\  |
   / \\  |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
   /    |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|\\  |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''',
    '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    '''
]


while len(lettre_mot) and vies > 0 :
    
    mot_à_trouver = [lettre if lettre in used_letters else '-'  for lettre in mot ]
    print("Mot à trouver :", " ".join(mot_à_trouver))
    print(f"Il te reste {vies} vies {pendu_images[vies]}\n voici les lettres que tu as déjà utilisé {" ".join(used_letters)}")
    print("\n")
    
    
    guess = input("Quelle lettre veux-tu tenter ? ").upper()
    print("\n")
    
    if guess in alphabet - used_letters : 
        used_letters.add(guess)
        if guess in lettre_mot :
            lettre_mot.remove(guess)
        else : 
            vies -= 1
            
    elif guess in used_letters : 
        print(f"Tu as déjà utilisé cette la lettre {guess}! Réessaye")
        continue 
    
    else : 
        print(f"{guess} n'est pas une lettre de l'alphabet. Réessaye")

    
    if guess == mot : 
        print(f"Bien joué !! Tu as trouvé le mot {mot} correctement !!")
        break 
        
    
if vies == 0 : 
    print(f"Malheureusement, tu n'as pas de deviner le mot {mot}")
else : 
    print(f"Bien joué !! Tu as trouvé le mot {mot} correctement !!")
