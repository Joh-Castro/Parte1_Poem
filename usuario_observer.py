class sistema_bancario():
	def cuenta_usuario_update(self):
		print("Hay un cambio en su cuenta bancaria")

class usuario():
	def ver_update(self):
		self.push = true

##########################

def principal():
	cambio_sistema_bancario = sistema_bancario()
	cambio_usuario = usuario()

	cambio_sistema_bancario.cuenta_usuario_update(cambio_usuario())
