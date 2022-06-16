from libr import suma

class Persona:

    personas = []

    def __init__(self, nombre, documento):
        self.name = nombre
        self.dni = documento
        Persona.personas.append(self)

    def dar_info( self ):
        return f'Name: {self.name}\nDni: {self.dni}\n'



a = Persona("Pepito", [1, 2, 3, 9, 6] )

b = Persona("Jorge", 314159265)
c = Persona("Pepito", 314159265)
d = Persona("Pepito", 314159265)

#print(a.contar_personas())
#print(Persona.contar_personas())

print(suma(2, 3))