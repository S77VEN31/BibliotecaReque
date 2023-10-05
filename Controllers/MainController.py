# Vistas
from Views import VistaMenuPrincipal
# Controladores
from Controllers import ControllerPrestarLibro
from Controllers import ControllerPrestarCubiculo
from Controllers import ControllerBiblioteca

class MainController:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.controllerBiblioteca = ControllerBiblioteca.ControllerBiblioteca(biblioteca=self.biblioteca)
        self.prestarLibro = ControllerPrestarLibro.ControllerPrestarLibro(biblioteca=self.biblioteca)
        self.prestarCubiculo = ControllerPrestarCubiculo.ControllerPrestarCubiculo(biblioteca=self.biblioteca)
        self.vista = VistaMenuPrincipal.VistaMenuPrincipal()  

    def menuPrincipal(self):
        opcion = self.vista.vistaMenuPrincipal()
        if opcion == "1":
            self.prestarLibro.controllerPrestarLibro()
        elif opcion == "2":
            self.prestarCubiculo.controllerPrestarCubiculo()
        elif opcion == "3":
            self.controllerBiblioteca.obtenerLibrosDisponibles() 
        elif opcion == "4":
            self.controllerBiblioteca.obtenerPrestamosLibros()
        elif opcion == "5":
            self.controllerBiblioteca.obtenerPrestamosLibrosPorFecha()
        elif opcion == "6":
            self.controllerBiblioteca.obtenerPrestamosCubiculos()
        elif opcion == "7":
            self.prestarLibro.devolverLibro()
        else:
            print("Opcion invalida")
        self.menuPrincipal()