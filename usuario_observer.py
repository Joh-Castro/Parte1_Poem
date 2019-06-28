class sistema_bancario():
	def cuenta_usuario_update(self):
		print("PUSH: Hay un cambio en su cuenta bancaria")

class usuario(sistema_bancario):
	def __init__(self):
		self.push = False

	def ver_update(self):
		self.push = True

##########################

cambio_cuenta_bancaria = usuario()
cambio_cuenta_bancaria.ver_update()
cambio_cuenta_bancaria.cuenta_usuario_update()
