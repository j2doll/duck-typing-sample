# duck-typing.py
'''
	code from https://en.wikipedia.org/wiki/Duck_typing
	
	"In other words, don't check whether it IS-a duck: check whether it QUACKS-like-a duck, WALKS-like-a duck, etc, etc, depending on exactly what subset of duck-like behaviour you need to play your language-games with."
		Alex Martelli 
'''

class Parrot:
	def fly(self):
		print("Parrot flying")

class Airplane:
	def fly(self):
		print("Airplane flying")

class Whale:
	def swim(self):
		print("Whale swimming")

def lift_off(entity):
	entity.fly()

parrot = Parrot()
airplane = Airplane()
whale = Whale()

lift_off(parrot) # prints `Parrot flying`
lift_off(airplane) # prints `Airplane flying`
lift_off(whale) # Throws the error `'Whale' object has no attribute 'fly'`
