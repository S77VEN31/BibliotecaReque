# Vistas
from Views import VistaPrestarCubiculo
# Controladores
from Controllers import ControllerBiblioteca
# Models
from Models import PrestamoCubiculo

class ControllerPrestarCubiculo:
    def __init__ (self, biblioteca):
        self.biblioteca = biblioteca
        self.vista = VistaPrestarCubiculo.VistaPrestarCubiculo()
        self.controllerBiblioteca = ControllerBiblioteca.ControllerBiblioteca(biblioteca=self.biblioteca)
   
    def crearPrestamoCubiculo(self, carnet, cubiculo):
        id = len(self.biblioteca.getPrestamosCubiculos()) + 1
        import datetime
        current_date = datetime.date.today()
        formatted_date = current_date.strftime("%d %m %Y")
        fechaFin = "30/10/2023"
        prestamoCubiculo = PrestamoCubiculo.PrestamoCubiculo(id, formatted_date, fechaFin, carnet, cubiculo)
        prestamosCubiculos = self.biblioteca.getPrestamosCubiculos()
        prestamosCubiculos.append(prestamoCubiculo)

    def controllerPrestarCubiculo(self):
        lista = self.vista.vistaPrestarCubiculo()
        opcion = lista[0]
        carnet = lista[1]
        if opcion == "1":
            cubiculo = self.controllerBiblioteca.buscarCubiculoConImpresora()
            if cubiculo:
                print("El cubiculo asignado es: " + str(cubiculo.getId()))
                self.crearPrestamoCubiculo(carnet, cubiculo)
            else:
                print("No hay cubiculos con impresora braile disponibles")
        if opcion == "2":
            cubiculo = self.controllerBiblioteca.getRandomCubiculo()
            if cubiculo:
                print("El cubiculo asignado es: " + str(cubiculo.getId()))
                self.crearPrestamoCubiculo(carnet, cubiculo)
            else:
                print("No hay cubiculos disponibles")

    