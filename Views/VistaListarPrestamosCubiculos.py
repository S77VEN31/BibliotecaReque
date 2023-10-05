class VistaListarPrestamosCubiculos:   
    def vistaListarPrestamosCubiculos(self, lista):
        if len(lista) == 0:
            print("No hay prestamos de cubiculos")
        else:
            for i in lista:
                print("\n=============================================\n")
                print("cubiculo: " ,i['cubiculo'])
                print("estudiante: " ,i['estudiante'])
                print("fecha prestamo: " ,i['fecha prestamo'])
                print("impresora: " ,i['impresora'])
                print("\n=============================================\n")        