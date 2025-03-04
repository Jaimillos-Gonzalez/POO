class Vehiculo:
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        print("Color: {}, {} Ruedas: ".format(self.color,self.ruedas))

class Coche(Vehiculo):
    def __init__(self,velocidad,color,ruedas):
        super().__init__(color,ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return "Soy un coche; " + super.__str__() + " y corro a {} kilómetros".format(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self,tipo,color,ruedas):
        super().__init__(color,ruedas)
        self.tipo = tipo

    def __str__(self):
        return "Soy una bici " + super.__str__() + "Soy una bici de tipo: {} y tengo {} ruedas".format(self.tipo, self.ruedas)

vehiculo =  Vehiculo("Rojo",4)

print(vehiculo)


        