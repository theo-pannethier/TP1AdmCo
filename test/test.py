#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 16:25:24 2022

export PYTHONPATH=$PYTHONPATH:"."
env|grep PYTHONPATH

python3 -m pylint Programme.py

@author: theo.pannethier
"""

from calculator.SimpleCalculator import SimpleCalculator
import unittest



OBJET = SimpleCalculator()
print (OBJET.sum2(10, 2))
print(OBJET.substract(10, 2))
print(OBJET.divide(10, 0))
print(OBJET.mul(10, 2))
