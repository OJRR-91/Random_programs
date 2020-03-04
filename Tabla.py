from __future__ import print_function
import sys
if len(sys.argv)==3:
    filas=int(sys.argv[1])
    columnas=int(sys.argv[2])
    if filas<1 or filas>9 or columnas<1 or columnas>9:
        print ("Error los parametros no pueden ser mayor de nuevo omenor de 1")
        print("Ejemplo: Tabla.py '1' '9'")
    else:
        for i in range(filas):
            print(" ")
            for c in range(columnas):
                print("*",end =" ")
else:
    print("ERROR parametros mal introducidos")