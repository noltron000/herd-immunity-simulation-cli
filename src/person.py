import random

from virus import Virus

random.seed(42)

################
# Person Class #
################

class Person:
	'''The simulation will contain people, who make up a population.'''

	@property
	def is_infected(self): return self.infection is not None

	def __init__(self, _id: int, is_vaccinated = False, infection: Virus | None = None):
		'''Initializes a new person.'''

		self._id = _id # type: int
		self.is_vaccinated = is_vaccinated # type: bool

		# We start out with `is_alive = True`, because we don't make vampires or zombies.
		# All other values are set by the simulation when it makes each Person object.
		self.is_alive = True # type: bool

		# If the person is chosen to be infected when the population is created,
		# then the simulation should instantiate a `Virus` object
		# and pass it into the instance via the `infection` parameter.
		# Otherwise, `infection` defaults to `None` (to represent no infection).
		self.infection = infection # type: Virus | None

		# This helps us find whether an infection is dormant or not later...
		# If there is no infection, then this must be set to `False`.
		self.is_dormant = False

	def resolve_exposure(self, virus: Virus):
		'''Determines whether or not a person gets sick from being exposed.'''

		if self.infection is not None:
			# The person is already sick, they can't get sick again.
			return False

		elif self.is_vaccinated:
			# The person is vaccinated. They can't get sick.
			return False

		# Randomly determine if the person gets sick,
		# based on the virus' reproduction rate.
		dice_roll = random.random()

		if dice_roll < virus.reproduction_rate:
			# The person gets infected...
			self.infection = virus
			self.is_dormant = True
			return True
		else:
			# The person got lucky!
			return False

	def resolve_infection(self):
		'''
		Generates a random number and compare it to the `mortality_rate`.
		If the random number is smaller, then `Person` dies from the disease.
		If the `Person` survives, then they become vaccinated, and they have no infection.
		Returns a boolean value indicating whether or not they survived the infection.
		'''

		if self.infection is None:
			# The person is not infected. They live.
			return True

		# Randomly determine if the person dies,
		# based on the virus' mortality rate.
		dice_roll = random.random()

		if dice_roll < self.infection.mortality_rate:
			# The person dies...
			self.is_alive = False
			self.is_vaccinated = False
			self.is_dormant = False
			self.infection = None
			return False
		else:
			# The person lives!
			self.is_vaccinated = True
			self.is_dormant = False
			self.infection = None
			return True
