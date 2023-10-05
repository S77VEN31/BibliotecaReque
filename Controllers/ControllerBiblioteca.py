# Vistas
from Views import VistaListarPrestamosLibros
from Views import VistaListarPrestamosLibrosPorFecha
from Views import VistaListarPrestamosCubiculos

class ControllerBiblioteca:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.vistaListar = VistaListarPrestamosLibros.VistaListarPrestamosLibros()
        self.vistaListarPorFecha = VistaListarPrestamosLibrosPorFecha.VistaListarPrestamosLibrosPorFecha()
        self.vistaLitarCubiculos = VistaListarPrestamosCubiculos.VistaListarPrestamosCubiculos()
    def obtenerLibros(self):
        return self.biblioteca.getLibros()
    def buscarLibro(self, isbn):
        for libro in self.biblioteca.getLibros():
            if libro.getISBN() == isbn:
                return libro
        return None
    def buscarCubiculoConImpresora(self):
        for cubiculo in self.biblioteca.getCubiculos():
            if cubiculo.getTieneImpresoraBraile() == True and cubiculo.getDisponible()[0] == True:
                cubiculo.setDisponible((False,))
                return cubiculo
        return None
    def getRandomCubiculo(self):
        for cubiculo in self.biblioteca.getCubiculos():
            if cubiculo.getDisponible()[0] == True:
                cubiculo.setDisponible((False,))
                return cubiculo
        return None
        
    def obtenerLibrosDisponibles(self):
        libros = self.obtenerLibros()
        for libro in libros:
            if libro.getDisponible() == True:
                print(libro.getTitulo())
    def generarDiccionarioLibros(self, lista, fecha = None):
        result = []
        for prestamo in lista:
            if fecha:
                if prestamo.getFechaInicio() != fecha:
                    continue
            dict = {
                "libro": prestamo.getLibro().getTitulo(),
                "estudiante": prestamo.getEstudiante().getNombre(),
                "fecha prestamo": prestamo.getFechaInicio()
            }
            result.append(dict)
        return result

    def obtenerPrestamosLibros(self):
        generarDiccionarioLibros = self.generarDiccionarioLibros(self.biblioteca.getPrestamosLibros())
        self.vistaListar.vistaListarPrestamosLibros(generarDiccionarioLibros )
    def obtenerPrestamosLibrosPorFecha(self):
        fecha = self.vistaListarPorFecha.vistaListarPrestamosLibrosPorFecha()
        generarDiccionarioLibros = self.generarDiccionarioLibros(self.biblioteca.getPrestamosLibros(), fecha)
        self.vistaListar.vistaListarPrestamosLibros(generarDiccionarioLibros)
    
    def obtenerPrestamosCubiculos(self):
        result = []
        for prestamo in self.biblioteca.getPrestamosCubiculos():
            dict = {
                "cubiculo": prestamo.getCubiculo().getId(),
                "estudiante": prestamo.getEstudiante(),
                "fecha prestamo": prestamo.getFechaInicio(),
                "impresora": prestamo.getCubiculo().getTieneImpresoraBraile()
            }
            result.append(dict)
            print(dict)
        self.vistaLitarCubiculos.vistaListarPrestamosCubiculos(result)
        
        
   
    