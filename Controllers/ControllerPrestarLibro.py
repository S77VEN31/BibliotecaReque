# Vistas
from Views import VistaPrestarLibro
from Views import VistaDevolverLibro
# Controladores
from Controllers import ControllerBiblioteca
class ControllerPrestarLibro:
    def __init__ (self, biblioteca):
        self.biblioteca = biblioteca
        self.controllerBiblioteca = ControllerBiblioteca.ControllerBiblioteca(biblioteca=self.biblioteca)
        self.vista = VistaPrestarLibro.VistaPrestarLibro()
        self.vistaDevolverLibro = VistaDevolverLibro.VistaDevolverLibro()
    def controllerPrestarLibro(self):
        opcion = self.vista.vistaPrestarLibro()
        if opcion == "1":
    
            isbn = input("Ingrese el ISBN del libro para buscarlo: ")
            libro = self.controllerBiblioteca.buscarLibro(isbn=isbn)
            if libro != None:
                if libro.getDisponible() == True:
                    libro.setDisponible(False)
                    print("El libro se presto correctamente")
                else:
                    print("El libro no esta disponible")
            else:
                print("El libro no existe")
        return
    def devolverLibro(self):
        carnet = self.vistaDevolverLibro.vistaDevolverLibro()
        prestamos = self.biblioteca.getPrestamosLibros()
        for prestamo in prestamos:
            if prestamo.getEstudiante().getId() == carnet:
                prestamo.getLibro().setDisponible(True)
                print("El libro se devolvio correctamente")
        new_prestamos = [prestamo for prestamo in prestamos if prestamo.getEstudiante().getId() != carnet]
        self.biblioteca.setPrestamosLibros(new_prestamos)






        