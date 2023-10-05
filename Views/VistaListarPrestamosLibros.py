class VistaListarPrestamosLibros:   
    def vistaListarPrestamosLibros(self, lista):
        if len(lista) == 0:
            print("No hay prestamos de libros")
        else:
            for i in lista:
                print("\n=============================================\n")
                print("libro: " ,i['libro'])
                print("estudiante: " ,i['estudiante'])
                print("fecha prestamo: " ,i['fecha prestamo'])
                print("\n=============================================\n")        