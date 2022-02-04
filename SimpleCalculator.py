#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 14:20:36 2022

@author: theo.pannethier
"""


class SimpleCalculator:
    def is_num_int(self, a):
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

    def sum2(self, a, b):
        """
        Entrée : 2 entiers
        Sortie : 1 entier

        Description : programme réalisant l'operation int(a)+int(b)
        """
        res = -1
        if self.is_num_int(a) and self.is_num_int(b):
            res = a + b
        return res

    def substract(self, a, b):
        """
        Entrée : 2 entiers avec b != 0
        Sortie : 1 entier

        Description : programme réalisant l'operation int(a)-int(b)
        """
        res = -1
        if self.is_num_int(a) and self.is_num_int(b):
            res = a - b
        return res

    def divide(self, a, b):
        """
        Entrée : 2 entiers
        Sortie : 1 float

        Description : programme réalisant l'operation int(a)/int(b)
        """
        res = -1
        if self.is_num_int(a) and self.is_num_int(b) and b != 0:
            res = a / b
        return res

    def mul(self, a, b):
        """
        Entrée : 2 entiers
        Sortie : 1 entier

        Description : programme réalisant l'operation int(a)*int(b)
        """
        res = -1
        if self.is_num_int(a) and self.is_num_int(b):
            res = a * b
        return res


print(SimpleCalculator.sum2(10, 2))
print(SimpleCalculator.substract(10, 2))
print(SimpleCalculator.divide(10, 2))
print(SimpleCalculator.mul(10, 2))
