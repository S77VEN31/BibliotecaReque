from Models import Biblioteca
from Models import Estudiante
from Models import Libro
from Models import PrestamoLibro
from Models import PrestamoCubiculo
from Models import Cubiculo

from Views import MenuPrincipal
# Call the constructor of the class Estudiante
estudiante1 = Estudiante.Estudiante(
    1, "Stiven", "Segura", "Cartago", "83043985", "stivensg313131@estudiantec.cr"
)
estudiante2 = Estudiante.Estudiante(
    2, "Juan", "Perez", "Cartago", "83043985", "stiven@hotmail.com"
)
# Call the constructor of the class Libro
libro1 = Libro.Libro(
    "La sirenita", "Ariel", "DevCorp", "0-4223-0450-6", "2019", True
)
libro2 = Libro.Libro(
    "La cenicienta", "Pablo", "DevCorp", "0-4223-0451-6", "2018", True
)

# Call the constructor of the class Cubiculo
cubiculo1 = Cubiculo.Cubiculo(1, 20, True, True)
cubiculo2 = Cubiculo.Cubiculo(2, 10, True, False)

# Call the constructor of the class Biblioteca
biblioteca = Biblioteca.Biblioteca(
    [estudiante1, estudiante2],
    [libro1, libro2], 
    [], 
    [],
    [cubiculo1, cubiculo2]
)



# Call the function menuPrincipal from the class MenuPrincipal
MenuPrincipal.MenuPrincipal.menuPrincipal()
