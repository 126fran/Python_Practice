# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:21:00 2021

@author: Francisco
"""

class MiClase():
    dato = 100
    def __init__(self,x):
        self.valor = x
    
    #sobrecarga del REPR (print) para retornar una cadena con el estado de la clase
    def __repr__(self):
        return "El valor es: " + str(self.valor) + "Y el dato es: " + str(MiClase.dato)
    
    #Este es un método de instancia, notar que se envia el SELF
    def MiMetodo(self,x):
        self.valor = x
        self.dato = x*10
        return "En mi metodo, ", self
    
    #Este es un método de clase, notar que se envia el CLS
    
    @classmethod
    def MetodoClase(cls,x):
        #no se puede usar self porque no hay acceso a él. Self representa una instancia
        cls.valor = x
        cls.dato = x*11
        return "En el metodo de clase: ", cls
    
    
    @staticmethod
    def MetodoEstatico(x):
        valor = x
        MiClase.dato = valor*12
        return "Metodo estatico no retorna valores en este caso"
    
    
    
#ahora instanciamos

MiObjeto = MiClase(10)
MiObjeto2 = MiClase(20)
print(MiObjeto)
print("----------------")

r = MiObjeto.MiMetodo(5)
print(r)
print(MiObjeto)
#Notar acá que el valor de dato no cambió porque lo tomamos del metodo __repr__ 
#que está buscando el valor en MiClase.dato y no en MiObjeto.dato

#Luego, si quiero saber el valor dato de la instancia, ejecuto lo siguiente
print(MiObjeto.dato)



r = MiObjeto.MetodoClase(3)
print(r)
print("Mi objeto")
#Notar acá que el valor no cambia, ya que cls.valor no existe. Valor es un atributo
#de instancia y no de clase. Por otra parte, el atributo dato es un atributo 
#de clase y por eso cls.dato si funciona y si cambia PARA TODAS LAS INSTANCIAS
print(MiObjeto)



r = MiClase.MetodoEstatico(7)
print(r)
#Notar que acá si cambia el atributo dato porque esta siendo invocado desde MiClase.dato
print(MiObjeto)
print("------")
#Notar que el atributo dato cambia también en MiObjeto2, ya que dato es una
#variable de clase
print(MiObjeto2)
