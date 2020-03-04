print("Ejercicio 1:")
edad=int(input("Ingresa tu edad "))
if edad>=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print("Ejercicio 2:")
contrasena=raw_input("Guarda una contrasena no importan mayusculas o minusculas ")
con=contrasena.lower()
cc=raw_input("Ingrese de nuevo la contrasena ")
c=cc.lower()
if con==c:
    print("Contrasena correcta")
else:
    print("Contrasena incorrecta")
print("Ejercicio 4:")
edad=int(input("Ingresa tu edad "))
ingreso=int(input("De cuanto son tus ingresos mensuales "))
if edad>=18 and ingreso>=1000:
    print("Ya es hora que te reportes al SAT")
else:
    print("No te preocupes aun no eres importante para el SAT")
print("Ejercicio 5:")
import string
a=string.ascii_lowercase
lista=[]
for i in a:
    lista.append(i)
sexo=raw_input("Ingresa tu genero M o F ").lower()
nombre=raw_input("Ingresa tu nombre ")
ind=nombre[0].lower()
for i in lista[0:13]:
    if i==ind and sexo=="f":
        print("Grupo A")
    if i==ind and sexo=="m":
        print("Grupo B")
for i in lista[14:]:
    if i==ind and sexo=="m":
        print("Grupo A")
    if i==ind and sexo=="f":
        print("Grupo B")
        