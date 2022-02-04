# -*- coding: utf-8 -*-
"""
Editeur : Theo PANNETHIER
Fonctions + - * / appliquées à 2 entiers.
"""
"glpat-WK1ijyydBZSg2TxjxsYG"
"""
FUNCTIONS
-------------------------------------------------------------------------------
"""


def is_num_int(a):
    """
    Entrée : 1 entier
    Sortie : 1 booleen

    Description : programme verifiant que a est un int
    """
    try:
        int(a)
        it_is = True
    except ValueError:
        it_is = False
    return it_is


def sum2(a, b):
    """
    Entrée : 2 entiers
    Sortie : 1 entier

    Description : programme réalisant l'operation int(a)+int(b)
    """
    res = -1
    if is_num_int(a) and is_num_int(b):
        res = a + b
    return res


def substract(a, b):
    """
    Entrée : 2 entiers avec b != 0
    Sortie : 1 entier

    Description : programme réalisant l'operation int(a)-int(b)
    """
    res = -1
    if is_num_int(a) and is_num_int(b):
        res = a - b
    return res


def divide(a, b):
    """
    Entrée : 2 entiers
    Sortie : 1 float

    Description : programme réalisant l'operation int(a)/int(b)
    """
    res = -1
    if is_num_int(a) and is_num_int(b) and b != 0:
        res = a / b
    return res


def mul(a, b):
    """
    Entrée : 2 entiers
    Sortie : 1 entier

    Description : programme réalisant l'operation int(a)*int(b)
    """
    res = -1
    if is_num_int(a) and is_num_int(b):
        res = a * b
    return res


"""
/FUNCTIONS
-------------------------------------------------------------------------------
"""


"""
MAIN
-------------------------------------------------------------------------------
"""

print(sum2("a", 1))
print(substract(10, 1))
print(divide(10, 1))
print(mul(10, 1))


"""
-------------------------------------------------------------------------------
/MAIN
"""
