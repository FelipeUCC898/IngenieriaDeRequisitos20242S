class totalmetroscubicos:

    def __init__(self):
        self.__metroscubicos = float(input("Introduce la base de la alberca: "))* (float(input("Introduzca la altura de la alberca: "))) *(float(input("Introduzca valor del ancho de la alberca")))
        self.VALORMETROCUBICO = 10000

    def consumoDeAguaAlberca(self):
        pago = self.__metroscubicos * self.VALORMETROCUBICO
        return pago
    
pago = totalmetroscubicos()     
metro = pago.consumoDeAguaAlberca()

print(f"El costo por metro cubico de agua de una alberca es: {metro}")