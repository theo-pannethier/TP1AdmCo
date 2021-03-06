#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 14:20:36 2022

@author: theo.pannethier
"""


class  SimpleCalculator:
    """
    Classe pour le calcul
    """

    def __init__(self):
        """
        inti
        """


    def sum2(self, a_int, b_int):
        """
        Entrée : 2 entiers
        Sortie : 1 entier

        Description : programme réalisant l'operation int(a)+int(b)
        """
        if isinstance(a_int,int) and isinstance(b_int,int):
            res = a_int + b_int
            return res
        print("ERRROR")
        return -1
            
    def substract(self, a_int, b_int):
        """
        Entrée : 2 entiers avec b != 0
        Sortie : 1 entier

        Description : programme réalisant l'operation int(a)-int(b)
        """
        if isinstance(a_int,int) and isinstance(b_int,int):
            res = a_int - b_int
            return res
        print("ERRROR")
        return -1

    def divide(self, a_int, b_int):
        """
        Entrée : 2 entiers
        Sortie : 1 float

        Description : programme réalisant l'operation int(a)/int(b)
        """
        if isinstance(a_int,int) and isinstance(b_int,int):
            if b_int !=0:
                res = a_int + b_int
                return res
            else:
                print('raise ZeroDivisionError("Cannot divide by zero")')
            
        print("ERRROR")
        return -1
            
    def mul(self, a_int, b_int):
        """
        Entrée : 2 entiers
        Sortie : 1 entier

        Description : programme réalisant l'operation int(a)*int(b)
        """
        if isinstance(a_int,int) and isinstance(b_int,int):
            res = a_int * b_int
            return res
        print("ERRROR")
        return -1

