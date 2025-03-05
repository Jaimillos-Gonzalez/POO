class Empleado:

    def __init__(self, nombrecompleto, cedula, telefono):
        self._nombrecompleto = nombrecompleto
        self._cedula = cedula
        self._telefono = telefono

    def __str__(self):
        return "{}, {}, {}".format(self._nombrecompleto, self._cedula, self._telefono)

    def set_nombre(self, nombrecompleto):
        self._nombrecompleto = nombrecompleto
    
    def get_nombre(self):
        return self._nombrecompleto
    
    def set_cedula(self, cedula):
        self._cedula = cedula

    def get_cedula(self):
        return self._cedula
    
    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_telefono(self):
        return self._telefono
    
class EmpleadoTiempoDefinido(Empleado):

    def __init__(self, nombrecompleto, cedula, telefono, numeroplaza, salariobase, duracioncontrato):
        super().__init__(nombrecompleto, cedula, telefono)
        self._numeroplaza = numeroplaza
        self._salariobase = salariobase
        self._duracioncontrato = duracioncontrato

    def set_numeroplaza(self, numeroplaza):
        self._numeroplaza = numeroplaza

    def get_numeroplaza(self):
        return self._numeroplaza
    
    def set_salariobase(self, salariobase):
        self._salariobase = salariobase

    def get_salariobase(self):
        return self._salariobase
    
    def set_duracioncontrato(self, duracioncontrato):
        self._duracioncontrato = duracioncontrato

    def get_duracioncontrato(self):
        return self._duracioncontrato
    
    def salariototal(self):
        salario = self._salariobase * 12
        salario = salario * 1.02
        return salario
    
class EmpleadoTiempoIndefinido(Empleado):

    def __init__(self, nombrecompleto, cedula, telefono, numeroplaza, salariobase, categoria):
        super().__init__(nombrecompleto, cedula, telefono)
        self._numeroplaza = numeroplaza
        self._salariobase = salariobase
        self._categoria = categoria
    
    def set_numeroplaza(self, numeroplaza):
        self._numeroplaza = numeroplaza

    def get_numeroplaza(self):
        return self._numeroplaza
    
    def set_salariobase(self, salariobase):
        self._salariobase = salariobase

    def get_salariobase(self):
        return self._salariobase
    
    def set_categoria(self, categoria):
        self._categoria = categoria

    def get_categoria(self):
        return self._categoria
    
    def calcula_salario_toatl(self):
        if(self._categoria == 1):
            return self._salariobase + (self._salariobase * 0.03)
        elif (self._categoria == 2):
            return self._salariobase + (self._salariobase * 0.05)
        elif (self._categoria == 3):
            return self._salariobase + (self._salariobase * 0.08)
        else:
            return 0
        
class EmpleadoSubcontratado(Empleado):
    def __init__(self, nombrecompleto, cedula, telefono, empresaresponsable):
        super().__init__(nombrecompleto, cedula, telefono)
        self._empresaresponsable = empresaresponsable

    def set_empresaresponsable(self, empresaresponsable):
        self._empresaresponsable = empresaresponsable

    def get_empresaresponsable(self):
        return self._empresaresponsable

subcontratado1 = EmpleadoSubcontratado("Luis Sub1","cedula1","1111","Tokiota")
subcontratado2 = EmpleadoSubcontratado("Antonio Sub2","cedula2","2222","Microsoft")

contratado1 = EmpleadoTiempoDefinido("Juan Defi1","cedula3","3333",2,35000,3)
contratado2 = EmpleadoTiempoDefinido("Nacho Defi2","cedula4","4444",3,37000,4)

indefinido1 = EmpleadoTiempoIndefinido("Jorge Indef1","cedula5","5555",5,43000,1)
indefinido2 = EmpleadoTiempoIndefinido("Manuel Indef2","cedula6","6666",6,46000,3)
indefinido3 = EmpleadoTiempoIndefinido("Jaime Indef3","cedula7","7777",7,48000,2)
indefinido4 = EmpleadoTiempoIndefinido("Marcelo Indef4","cedula8","8888",9,49000,2)

# empleado = Empleado("Jaime Gonzalez","cedula1", "600112233")
# print(empleado)
