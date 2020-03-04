class triangulo():
    def area(self):
        b=float(input("Introduce la base del triangulo "))
        a=float(input("Introduce la altura del triangulo "))
        area=(b*a)/2
        print(area)
class rectangulo():
    def area(self):
        b=float(input("Ingresa la base del rectangulo "))
        a=float(input("Ingresa la altura del rectangulo "))
        area=(b*a)
        print(area)
class cuadrado():
    def area(self):
        l=float(input("Ingresa el valor de un lado del cuadrado "))
        area=(l*l)
        print(area)
        
opc=input("1.-Triangulo 2.-Rectangulo 3.-Cuadrado ")

if opc==1:
    at=triangulo()
    at.area()
if opc==2:
    ar=rectangulo()
    ar.area()
if opc==3:
    ac=cuadrado()
    ac.area()