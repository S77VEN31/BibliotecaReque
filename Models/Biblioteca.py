class Biblioteca:
    # Constructor
    def __init__(self, estudiantes, libros, prestamosLibros, prestamosCubiculos, cubiculos):
        self.estudiantes = estudiantes
        self.libros = libros
        self.prestamosLibros = prestamosLibros
        self.prestamosCubiculos = prestamosCubiculos
        self.cubiculos = cubiculos

    # Setters y Getters
    def setEstudiantes(self, estudiantes):
        self.estudiantes = estudiantes
    def setLibros(self, libros):
        self.libros = libros
    def setPrestamosLibros(self, prestamosLibros):
        self.prestamosLibros = prestamosLibros
    def setPrestamosCubiculos(self, prestamosCubiculos):
        self.prestamosCubiculos = prestamosCubiculos
    def setCubiculos(self, cubiculos):
        self.cubiculos = cubiculos
    def getEstudiantes(self):
        return self.estudiantes
    def getLibros(self):
        return self.libros
    def getPrestamosLibros(self):
        return self.prestamosLibros
    def getPrestamosCubiculos(self):
        return self.prestamosCubiculos
    def getCubiculos(self):
        return self.cubiculos
    