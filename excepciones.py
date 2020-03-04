# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:13:43 2019

@author: oscarjex
"""
"""while(True):
 n=float(input("Introduce un numero "))
 try:
    print("El resultado es {}").format(10/n)
    break
 except ZeroDivisionError:
    print("Introduce un numero diferetente de 0")
 except Exception as e:
    print(type(e))
lista=[1,2,3,4,5]
try:
   print( lista[10])
except  IndexError:
    print("No cuenta con ese indice la lista")
except Exception as e:
    print(type(e))"""
alumnos=[['oscar', 100], ['carlos', 60], ['sergio', 65], ['migue', 65]]
h=0
dic=dict(alumnos)
cal=[]
for i in range(0,len(alumnos)):
    cal.append(alumnos[i][1])
    if alumnos[h][1]>alumnos[i][1]:
       h=i
b=sorted(cal)
print(alumnos[h])
print(b)
q=0
for i in range(0,len(alumnos)):
    if b[q]==b[q+1]:
        q=q+1
if b[0]<b[1] and b[1]<b[2]:
        print("segundo peor,{}").format(b[1])
if b[1]==b[2]:
    
    print("segundo peores {}").format(b[1])
    
    