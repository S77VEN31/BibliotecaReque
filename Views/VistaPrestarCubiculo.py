class VistaPrestarCubiculo:
    def vistaPrestarCubiculo(self):
        print("\n=============================================\n")
        print("Prestar Cubiculo")
        print("1. Prestar Cubiculo con impresora braile")
        print("2. Prestar Cubiculo sin impresora braile")
        opcion = input("Ingrese una opcion: ")
        carnet = input("Ingrese carnet del estudiante:")
        print("\n=============================================\n")
        
        return [opcion, carnet]