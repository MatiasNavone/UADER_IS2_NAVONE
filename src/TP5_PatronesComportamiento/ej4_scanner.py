import os
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#* Extendido: agrega memorias M1-M4 (AM o FM) al ciclo de barrido
#*--------------------------------------------------------------------

"""State class: Base State class"""
class State:

	def scan(self):
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):
		self.radio    = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos      = 0
		self.name     = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
class FmState(State):

	def __init__(self, radio):
		self.radio    = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos      = 0
		self.name     = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

#*------- NUEVO: implementa el barrido de memorias M1-M4
class MemoryState(State):
	"""
	Estado que recorre las frecuencias memorizadas (M1-M4).
	Cada memoria puede ser AM o FM con su frecuencia especifica.
	Al terminar el barrido de las 4 memorias vuelve al estado FM.
	"""

	def __init__(self, radio):
		self.radio = radio
		# Cada memoria: (etiqueta, banda, frecuencia)
		self.stations = [
			("M1", "FM",  "98.3"),
			("M2", "FM", "103.7"),
			("M3", "AM",  "590"),
			("M4", "AM", "1240"),
		]
		self.pos  = 0
		self.name = "MEM"

	def scan(self):
		"""Recorre las memorias una a una; al terminar las 4 vuelve a FM."""
		etiqueta, banda, frecuencia = self.stations[self.pos]
		unidad = "MHz" if banda == "FM" else "kHz"
		print("Sintonizando... Memoria {} -> {} {} {}".format(
			etiqueta, banda, frecuencia, unidad))
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
			print("-- Fin de memorias, volviendo a FM --")
			self.radio.state = self.radio.fmstate

	def toggle_amfm(self):
		print("Cambiando a FM desde Memorias")
		self.radio.state = self.radio.fmstate


#*--------- Construye la radio con todas sus formas de sintonia
class Radio:

	def __init__(self):
		self.fmstate  = FmState(self)
		self.amstate  = AmState(self)
		self.memstate = MemoryState(self)   # NUEVO

		# Inicialmente en FM
		self.state = self.fmstate

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		self.state.scan()

	def scan_memories(self):
		"""NUEVO: activa el estado de memorias y barre las 4 frecuencias."""
		self.state = self.memstate
		print("\n-- Iniciando barrido de memorias --")
		for _ in range(len(self.memstate.stations)):
			self.scan()

#*---------------------

if __name__ == "__main__":
	os.system("clear")
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()

	# Secuencia original: 3 scan FM + toggle + 3 scan AM, repetida 2 veces
	actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
	actions *= 2

	print("Recorre las acciones ejecutando la accion, el objeto cambia la interfaz segun el estado")
	for action in actions:
		action()

	# NUEVO: al finalizar el ciclo se barren las 4 memorias
	print("\n========================================")
	print("Barrido de frecuencias memorizadas M1-M4")
	print("========================================")
	radio.scan_memories()