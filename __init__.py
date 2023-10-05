from Models import Biblioteca
from Models import Estudiante
from Models import Libro
from Models import Cubiculo
from Models import PrestamoLibro

from Controllers import MainController


# Call the constructor of the class Estudiante
estudiante1 = Estudiante.Estudiante(
    "1", "Stiven", "Segura", "Cartago", "83043985", "stivensg313131@estudiantec.cr"
)
estudiante2 = Estudiante.Estudiante(
    "2", "Juan", "Perez", "Cartago", "83043985", "stiven@hotmail.com"
)
# Call the constructor of the class Libro
libro1 = Libro.Libro(
    "La sirenita", "Ariel", "DevCorp", "1", "2019", False
)
libro2 = Libro.Libro(
    "La cenicienta", "Pablo", "DevCorp", "2", "2018", False
)
libro3 = Libro.Libro(
    "La bella durmiente", "Juan", "DevCorp", "3", "2017", True
)
prestamoLibro1 = PrestamoLibro.PrestamoLibro(
    1, '01-01-2020', '01-02-2020', libro1, estudiante1
)
prestamoLibro2 = PrestamoLibro.PrestamoLibro(
    2, '02-01-2020', '01-02-2020', libro2, estudiante2
)


# Call the constructor of the class Cubiculo
cubiculo1 = Cubiculo.Cubiculo(1, 20, True, True)
cubiculo2 = Cubiculo.Cubiculo(2, 10, True, False)
cubiculo3 = Cubiculo.Cubiculo(3, 30, False, True)
cubiculo4 = Cubiculo.Cubiculo(4, 40, False, False)
cubiculo5 = Cubiculo.Cubiculo(5, 50, True, True)

# Call the constructor of the class Biblioteca
biblioteca = Biblioteca.Biblioteca(
    [estudiante1, estudiante2],
    [libro1, libro2, libro3], 
    [prestamoLibro1, prestamoLibro2], 
    [],
    [cubiculo1, cubiculo2, cubiculo3, cubiculo4, cubiculo5]
)
 
mainController = MainController.MainController(biblioteca=biblioteca)
mainController.menuPrincipal()






