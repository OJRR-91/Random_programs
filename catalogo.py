class Pelicula:
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo=titulo
        self.duracion=duracion
        self.lanzamiento=lanzamiento
        print("Se ha creado la pelicual {}.".format(self.titulo))
    def __str__(self):
        return "{} , {}.".format(self.titulo,self.lanzamiento)
class Catalogo:
    peliculas=[]
    def __init__(self,peliculas=[]):
        self.peliculas=peliculas
    def agregar(self,p):
        self.peliculas.append(p)
    def mostrar(self):
        for p in self.peliculas:
            print(p)           

