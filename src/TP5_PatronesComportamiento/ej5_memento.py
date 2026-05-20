import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#* Extendido: historial de hasta 4 estados, undo(n) para recuperar
#* cualquiera de ellos (n=0 inmediato anterior, n=1,2,3 los previos)
#*--------------------------------------------------------------------

class Memento:
	def __init__(self, file, content):
		self.file    = file
		self.content = content


class FileWriterUtility:

	def __init__(self, file):
		self.file    = file
		self.content = ""

	def write(self, string):
		self.content += string

	def save(self):
		return Memento(self.file, self.content)

	def undo(self, memento):
		self.file    = memento.file
		self.content = memento.content


class FileWriterCaretaker:
	"""
	Gestor de mementos extendido.
	Almacena hasta MAX_HISTORY=4 estados.
	undo(writer, n):
	  n=0 -> estado inmediato anterior (history[-1])
	  n=1 -> history[-2]
	  n=2 -> history[-3]
	  n=3 -> history[-4] (el mas antiguo disponible)
	"""

	MAX_HISTORY = 4

	def __init__(self):
		self.history = []   # lista de Mementos, orden cronologico

	def save(self, writer):
		"""Guarda el estado actual. Si supera MAX_HISTORY descarta el mas antiguo."""
		memento = writer.save()
		self.history.append(memento)
		if len(self.history) > self.MAX_HISTORY:
			self.history.pop(0)
		print("  [Caretaker] Estado guardado. Historial: {} entradas".format(len(self.history)))

	def undo(self, writer, n=0):
		"""
		Recupera el estado en la posicion n hacia atras.
		n=0 -> el mas reciente; n=3 -> el mas antiguo guardado.
		"""
		if not self.history:
			print("  [Caretaker] No hay estados en el historial.")
			return

		if n < 0 or n >= self.MAX_HISTORY:
			print("  [Caretaker] n debe estar entre 0 y {}.".format(self.MAX_HISTORY - 1))
			return

		idx = -(n + 1)   # n=0 -> -1, n=1 -> -2, etc.
		if abs(idx) > len(self.history):
			print("  [Caretaker] No hay suficiente historial para n={}. Maximo disponible: n={}.".format(
				n, len(self.history) - 1))
			return

		writer.undo(self.history[idx])
		print("  [Caretaker] undo(n={}) aplicado.".format(n))


#*---------------------

if __name__ == '__main__':

	os.system("clear")

	print("Crea un objeto que gestionara la version anterior")
	caretaker = FileWriterCaretaker()

	print("Crea el objeto cuyo estado se quiere preservar")
	writer = FileWriterUtility("GFG.txt")

	# ── Estado 1 ──────────────────────────────
	print("\nSe graba algo en el objeto y se salva")
	writer.write("Clase de IS2 en UADER\n")
	print(writer.content)
	caretaker.save(writer)

	# ── Estado 2 ──────────────────────────────
	print("Se graba informacion adicional")
	writer.write("Material adicional de la clase de patrones\n")
	print(writer.content)
	caretaker.save(writer)

	# ── Estado 3 ──────────────────────────────
	print("Se graba informacion adicional II")
	writer.write("Material adicional de la clase de patrones II\n")
	print(writer.content)
	caretaker.save(writer)

	# ── Estado 4 ──────────────────────────────
	print("Se graba informacion adicional III")
	writer.write("Material adicional de la clase de patrones III\n")
	print(writer.content)
	caretaker.save(writer)

	# ── Estado 5: desborda el historial, descarta el 1 ──
	print("Se graba informacion adicional IV (desborda historial)")
	writer.write("Material adicional de la clase de patrones IV\n")
	print(writer.content)
	caretaker.save(writer)

	# ── Undo n=0: inmediato anterior ──────────
	print("\nse invoca al <undo(0)> -> estado inmediato anterior")
	caretaker.undo(writer, 0)
	print("Estado actual:")
	print(writer.content)

	# ── Undo n=1 ──────────────────────────────
	print("se invoca al <undo(1)> -> dos posiciones atras")
	caretaker.undo(writer, 1)
	print("Estado actual:")
	print(writer.content)

	# ── Undo n=3: el mas antiguo disponible ───
	print("se invoca al <undo(3)> -> el mas antiguo disponible")
	caretaker.undo(writer, 3)
	print("Estado actual:")
	print(writer.content)

	# ── Undo con n fuera de rango ─────────────
	print("se invoca al <undo(5)> -> fuera de rango")
	caretaker.undo(writer, 5)