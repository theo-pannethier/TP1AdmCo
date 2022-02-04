# -*- coding: utf-8 -*-
"""
Editeur : Theo PANNETHIER
Fonctions + - * / appliquées à 2 entiers.
"""


#FUNCTIONS
#-------------------------------------------------------------------------------


def is_num_int(a_int):
    """
    Entrée : 1 entier
    Sortie : 1 booleen

    Description : programme verifiant que a est un int
    """
    try:
        int(a_int)
        it_is = True
    except ValueError:
        it_is = False
    return it_is


def sum2(a_int, b_int):
    """
    Entrée : 2 entiers
    Sortie : 1 entier

    Description : programme réalisant l'operation int(a)+int(b)
    """
    res = -1
    if is_num_int(a_int) and is_num_int(b_int):
        res = a_int + b_int
    return res


def substract(a_int, b_int):
    """
    Entrée : 2 entiers avec b != 0
    Sortie : 1 entier

    Description : programme réalisant l'operation int(a)-int(b)
    """
    res = -1
    if is_num_int(a_int) and is_num_int(b_int):
        res = a_int - b_int
    return res


def divide(a_int, b_int):
    """
    Entrée : 2 entiers
    Sortie : 1 float

    Description : programme réalisant l'operation int(a)/int(b)
    """
    res = -1
    if is_num_int(a_int) and is_num_int(b_int) and b_int != 0:
        res = a_int / b_int
    return res


def mul(a_int, b_int):
    """
    Entrée : 2 entiers
    Sortie : 1 entier

    Description : programme réalisant l'operation int(a)*int(b)
    """
    res = -1
    if is_num_int(a_int) and is_num_int(b_int):
        res = a_int * b_int
    return res



#/FUNCTIONS
#-------------------------------------------------------------------------------


#MAIN
#-------------------------------------------------------------------------------


#print(sum2("a", 1))
#print(substract(10, 1))
#print(divide(10, 1))
#print(mul(10, 1))
#


#-------------------------------------------------------------------------------
#/MAIN
