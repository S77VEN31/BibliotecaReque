class Estudiante: 
    # Constructor
    def __init__(self, id, nombre, apellido, direccion, telefono, email):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
    # Getters y Setters
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    def setApellido(self, apellido):
        self.apellido = apellido
    def getApellido(self):
        return self.apellido
    def setDireccion(self, direccion):
        self.direccion = direccion
    def getDireccion(self):
        return self.direccion
    def setTelefono(self, telefono):
        self.telefono = telefono
    def getTelefono(self):
        return self.telefono
    def setEmail(self, email):
        self.email = email
    def getEmail(self):
        return self.email