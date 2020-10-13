import math

OPERATIONS = ['*', '-', '+', '/', '^']
FUNCTIONS = ['√', "SIN", "COS", "TAN"]

"""
Complexité de O(1)
"""
def VIDE():
    return None

"""
Complexité de O(1)
"""
def SOMMET(L):
    return L[0]

"""
Complexité de O(1)
"""
def CONS(x,L):
    return (x,L)

"""
Complexité de O(1)
"""
def EMPILER(L, ptr, x):
    return CONS(x,L)

"""
Complexité de O(1)
"""
def DEPILER(L, ptr):
    if EST_VIDE(L):
        return "ERR"
    return (SOMMET(L),L[1])

"""
Complexité de O(1)
"""
def EST_VIDE(L):
    return L is None

"""
Complexité de O(n)
Le code sera exécuté de manière récursive n fois (avec n le nombre d'élement dans la pile L)
Nombre d'exécution de la fonction de boucle:
    - longeur de L = 0 » 0 fois
    - longeur de L >= 1 » (nombre d'élement dans la pile L) fois
"""
def COMPTE(L):
    if EST_VIDE(L):
        return 0
    return 1 + COMPTE(L[1])

"""
Complexité de O(1)
"""
def LISTE_TO_PILE(L):
    P = VIDE()
    ptr = -1
    for x in L:
        P = EMPILER(P, ptr, x)
        ptr += 1
    
    return P

"""
'CH in OPERATIONS' (ligne 74) » complexité de O(n) avec n la longeur de la liste OPERATIONS (ligne 3)
'CH in FUNCTIONS' (ligne 75) » complexité de O(n) avec n la longeur de la liste FUNCTIONS (ligne 4)
On a donc une complexité de: O(len(OPERATIONS)*len(FUNCTIONS))
"""
def TYPE(CH):
    if CH in OPERATIONS:
        return "O"
    elif CH in FUNCTIONS:
        return "F"
    else:
        return "N"

"""
Complexité de O(1)
"""
def CALC_FONC(N1, FUN):
    if FUN == "√":
        return math.sqrt(float(N1))
    elif FUN == "SIN":
        return math.sin(float(N1))
    elif FUN == "COS":
        return math.cos(float(N1))
    elif FUN == "TAN":
        return math.tan(float(N1))
    
"""
Complexité de O(1)
N1 et N2 sont des string et sont convertie en float plutôt qu'en int pour supporter les potentiels valeur float
"""
def CALC_OP(N1, OP, N2):
    if OP == "*":
        return str(float(N1)*float(N2))
    if OP == "^":
        return str(float(N1)**float(N2))
    if OP == "/":
        return str(float(N1)/float(N2))
    if OP == "-":
        return str(float(N1)-float(N2))
    if OP == "+":
        return str(float(N1)+float(N2))

"""
Complexité de O(n)
La boucle for est executé n fois avec n la longeur de la pile exp
"""
def CALC_EXP(EXP, n):
    pile = VIDE()
    ptr = -1
    for _ in range(n):
        s, EXP = DEPILER(EXP, ptr)
        if TYPE(s) == "N":
            pile = EMPILER(pile, ptr, s)
            ptr += 1
        elif TYPE(s) == "O":
            n1, pile = DEPILER(pile, ptr)
            ptr -= 1
            n2, pile = DEPILER(pile, ptr)
            ptr -= 1
            """
            On met d'abord n2 puis n1 car lorsqu'il sont dépiler ils sont retourner et donc en cas d'opération telle que ^,
            les deux chiffres ou nombre sont inversé et donc on obtient le mauvais résultat: exemple 2^8 au lieu de 8^2
            """
            v = CALC_OP(n2, s, n1)
            print(f"Calcul en cours: {n2} {s} {n1}")
            pile = EMPILER(pile, ptr, v)
            ptr += 1
        elif TYPE(s) == "F":
            n3, pile = DEPILER(pile, ptr)
            ptr -= 1
            v = CALC_FONC(n3, s)
            print(f"Calcul en cours: {s} {n3}")
            pile = EMPILER(pile, ptr, v)
        else:
            print("ERR")
            return
    return pile

"""
Pour mettre n'impotre quel valeur postefixé rapidement, on peutrentrer les valeurs dans la console,
on peut enlevé le commentaire ligne 153 et 154 puis mettre en commentaire la ligne 152
Autrement, il faudra rentrer comme valeur dans la console ceci pour avoir le résultat de l'exercice: 2 5 + 4 5 3 + 2 ^ * √ *
Complexité de O(n) pour la ligne 151
"""
liste = ["2", "5", "+", "4", "5", "3", "+", "2", "^", "*", "√", "*"]
#liste = input("Entrez une expression postfixé: ")
#liste = liste.split(" ")

"""
Complexité de O(n) pour la ligne 160 afin de retourner la pile pour éviter dans la fonction "LISTE_TO_PILE"
d'avoir à dépiler la pile dans une autre
"""
liste = reversed(liste) 
L = LISTE_TO_PILE(liste)
RESULT = SOMMET(CALC_EXP(L, COMPTE(L)))
print("Résultat: " + str(RESULT))

"""
On a donc une complexité totale:
    - Programme principale de O(3n)
    - Fonctions utilitaire: O(n+9)
Soit une complexité total de O(4n+9)
"""