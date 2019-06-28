class reino_animal():
	
	def __init__(self, nombre_animal, color_animal, peso_animal):
		self.nombre_animal = nombre_animal
		self.color_animal = color_animal
		self.peso_animal = peso_animal

	def movimiento(self, en_movimiento):
		if en_movimiento:
			print("Que hace?: esta en movimiento")
		else:
			print("Que hace?: dormir")

	def caracteristicas(self):
		print ("Nombre:",self.nombre_animal, " Color:", self.color_animal, " Peso:", self.peso_animal)

#######################

class mamiferos(reino_animal):
	def andar(self):
		return "andando"

class aves(reino_animal):
	def volar(self):
		return "volando"

class reptiles(reino_animal):
	def arrastrarse(self):
		return "arrastrandose"

class insectos(reino_animal):
	pass

class peces(reino_animal):
	def nadar(self):
		return "nadando"

#"humanos" son del reino animal y ademas pueden hacer todos los metodos de las anteriores clases
class humanos(mamiferos,aves,reptiles,peces):
	pass

#####################
## Ejemplos #########
mi_perro = mamiferos("schiandra","blanca con manchas", "6 kilos")
mi_canario = aves("zucker","verde", "150 gramos")
soy_humano = humanos("johnny", "test blanca", "65 kilos")

mi_perro.caracteristicas()
mi_perro.movimiento(True)
print(mi_perro.andar())

mi_canario.caracteristicas()
mi_canario.movimiento(True)
print(mi_canario.volar())

soy_humano.caracteristicas()
soy_humano.movimiento(True)
print(soy_humano.andar())
print(soy_humano.nadar())
####################