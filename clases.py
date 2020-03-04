# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 11:55:49 2020

@author: oscarjex
"""

class Promedio():
    n1=0
    n2=0
    n3=0
    h=3
    pro=0
    def __init__(self):
        print("Se acaba de crear un objeto")
    def promedio(self):
        self.n1=int(input("Ingresa la calificacion del primer parcial "))
        self.n2=int(input("Ingresa la calificacion del segundo parcial "))
        self.n3=int(input("Ingresa la calificacion del tercer parcial "))
        pro=(self.n1+self.n2+self.n3)/self.h)
        print("El promedio es: ")