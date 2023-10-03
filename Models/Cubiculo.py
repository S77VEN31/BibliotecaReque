class Cubiculo:
    # Constructor
    def __init__(self, id, capacidad, disponible, tieneImpresoraBraile):
        self.id = id
        self.capacidad = capacidad
        self.disponible = disponible,
        self.tieneImpresoraBraile = tieneImpresoraBraile
    # Getters y Setters  
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id
    def setCapacidad(self, capacidad):
        self.capacidad = capacidad
    def getCapacidad(self):
        return self.capacidad
    def setDisponible(self, disponible):
        self.disponible = disponible
    def getDisponible(self):
        return self.disponible
    def setTieneImpresoraBraile(self, tieneImpresoraBraile):
        self.tieneImpresoraBraile = tieneImpresoraBraile
    def getTieneImpresoraBraile(self):
        return self.tieneImpresoraBraile
