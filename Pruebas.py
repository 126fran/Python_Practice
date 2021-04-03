# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 03:05:08 2021

@author: Francisco
"""

def prueba(a,b):
    if a > b:
        may = a
    else:
        may = b
    return may

print(prueba(7,6))

class Persona():
    def __init__(self,nombre = '',edad = 0):
        self.nombre = nombre
        self.edad = edad
        
jorge = Persona("Jorge",24)

print(jorge.nombre)
print(jorge.edad)
