from virus import Virus


def test_virus_instantiation():
	'''
	Check to make sure that the `Virus` instantiator is working.
	'''

	virus = Virus("HIV", 0.8, 0.3)
	assert virus.name == "HIV"
	assert virus.reproduction_rate == 0.8
	assert virus.mortality_rate == 0.3
def test_other_virus():
	virus = Virus("Influenza", 0.5, 0.1)

	assert virus.name == "Influenza"
	assert virus.reproduction_rate == 0.5
	assert virus.mortality_rate == 0.1
