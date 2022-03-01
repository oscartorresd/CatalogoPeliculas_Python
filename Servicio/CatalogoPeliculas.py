
import os

class CatalogoPeliculas:
    ruta_archivo="peliculas.txt"
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, "a", encoding="utf8")  as archivo:
            archivo.write(f"{pelicula.nombre}\n")
            print("Pelicula Agregada con exito")

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, "r", encoding="utf8") as archivo:
            print("catalogo peliculas".center(50,"-"))
            print(archivo.read())
    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta_archivo)
        print("archivo elininado: ", cls.ruta_archivo)

