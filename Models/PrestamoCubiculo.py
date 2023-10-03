class PrestamoCubiculo:
    # Constructor
    def __init__(self, id, fechaInicio, fechaFin, estudiante, cubiculo):
        self.id = id
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.estudiante = estudiante
        self.cubiculo = cubiculo
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
    def setEstudiante(self, estudiante):
        self.estudiante = estudiante
    def getEstudiante(self):
        return self.estudiante
    def setCubiculo(self, cubiculo):
        self.cubiculo = cubiculo
    def getCubiculo(self):
        return self.cubiculo