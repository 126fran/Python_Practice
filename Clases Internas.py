# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:50:42 2021

@author: Francisco
"""
#Clase externa
class Estudiante():
    def __init__(self,nombre,carrera):
        self.nombre = nombre
        self.carrera = carrera
        self.miLibro = self.Libro('Programacion','Francisco')
        
    def muestra(self):
        print("Me llamo " + self.nombre + " Y estudio " + self.carrera)
        self.miLibro.bibliografia()
        
    #Clase interna
    class Libro():
        def __init__(self,titulo,autor):
            self.titulo = titulo
            self.autor = autor
        
        def bibliografia(self):
            print("Titulo: " + self.titulo + " Autor: " + self.autor)
            
            
estudiante1 = Estudiante("Francisco", "Ingeniería")
estudiante1.muestra()

#Notar que podemos acceder a la clase interna siguiendo todo el caminito
#para eso entramos por estudiante1 y luego a miLibro que es el objeto instanciado
#de la clase Libro dentro de Estudiante.

#titulo pertenece a miLibro, pero miLibro pertenece a estudiante1
print("estoy leyendo: " + estudiante1.miLibro.titulo)

#Tambien podemos ejecutar metodos de la clase interna
estudiante1.miLibro.bibliografia()

#Tambien podemos crear nuevas instancias de la clase interna

otroLibro = Estudiante.Libro("El señor de los anillos", "Tolkien")
otroLibro.bibliografia()
