from Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas

opcion=None
while opcion!=4:
    try:
        print("opciones".center(50,"-"))
        print("1) Agregar Pelicula")
        print("2) listar Peliculas")
        print("3) Eliminar Catologo Peliculas")
        print("4) Salir")
        opcion=int(input("Ingrese una opcion entre 1 y 4: "))
        if opcion==1:
            nombre=input("Ingrese  el nombre de la pelicula: ")
            Pelicula=Pelicula(nombre)
            CatalogoPeliculas.agregar_pelicula(Pelicula)
        elif opcion==2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion==3:
            CatalogoPeliculas.eliminar()
    except Exception as e:
        print("opcion invalida ingrese un numero entre 1 y 4", e)
        opcion=None
    else:
        print("Fin del programa")