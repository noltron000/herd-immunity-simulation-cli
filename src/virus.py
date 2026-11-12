###############
# Virus Class #
###############

class Virus:
	'''
	Represents the virus that will be used
	to infect people within the `Simulation` class.
	'''

	def __init__(
			self,
			name: str,
			reproduction_rate: float,
			mortality_rate: float,
		):
		'''
		Sets up the virus to include its name,
		the reproduction rate that controls how infectious it is,
		and the mortality rate representing how deadly it is.
		'''

		self.name = name # type: str
		self.reproduction_rate = reproduction_rate # type: float
		self.mortality_rate = mortality_rate # type: float
