class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: {}, Ruedas: {}".format(self.color,str(self.ruedas))

class Coche(Vehiculo):
    def __init__(self,velocidad,color,ruedas):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return "Soy un coche; " + super().__str__() + " y corro a {} kilómetros".format(str(self.velocidad))

class Bicicleta(Vehiculo):
    def __init__(self,tipo,color,ruedas):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return "Soy una bici " + super().__str__() + " y soy del tipo: {}".format(self.tipo)

vehiculo =  Vehiculo("Rojo",4)
coche = Coche(100,"Azul",4)
bici = Bicicleta("Gravel","negra",2)

print(vehiculo)
print(coche)
print(bici)


        