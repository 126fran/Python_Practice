# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:09:08 2021

@author: Francisco
"""

class Product():
    def __init__(self,nombre='',precio=0,descripcion=''):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

mermelada = Product("Mermelada",35,"Una mermelada de durazno")

print(mermelada.nombre)
print(mermelada.precio)
print(mermelada.descripcion)