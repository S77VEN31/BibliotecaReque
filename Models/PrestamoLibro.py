class PrestamoLibro:
    # Constructor
    def __init__(self, id, fechaInicio, fechaFin, libro, estudiante):
        self.id = id
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.libro = libro
        self.estudiante = estudiante
    # Getters y Setters
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id
    def setFechaInicio(self, fechaInicio):
        self.fechaInicio = fechaInicio
    def getFechaInicio(self):
        return self.fechaInicio
    def setFechaFin(self, fechaFin):
        self.fechaFin = fechaFin
    def getFechaFin(self):
        return self.fechaFin
    def setLibro(self, libro):
        self.libro = libro
    def getLibro(self):
        return self.libro
    def setEstudiante(self, estudiante):
        self.estudiante = estudiante
    def getEstudiante(self):
        return self.estudiante
