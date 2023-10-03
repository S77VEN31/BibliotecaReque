class Libro:
    # Constructor
    def __init__(self, titulo, autor, editorial, isbn, publicacion, disponible):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.ISBN = isbn
        self.publicacion = publicacion
        self.disponible = disponible
    # Getters y Setters
    def setTitulo(self, titulo):
        self.titulo = titulo
    def getTitulo(self):
        return self.titulo
    def setAutor(self, autor):
        self.autor = autor
    def getAutor(self):
        return self.autor
    def setEditorial(self, editorial):
        self.editorial = editorial
    def getEditorial(self):
        return self.editorial
    def setISBN(self, isbn):
        self.ISBN = isbn    
    def getISBN(self):
        return self.ISBN
    def setPublicacion(self, publicacion):
        self.publicacion = publicacion
    def getPublicacion(self):
        return self.publicacion
    def setDisponible(self, disponible):
        self.disponible = disponible
    def getDisponible(self):
        return self.disponible
    
    
