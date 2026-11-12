from virus import Virus


def test_virus_instantiation():
	'''
	Check to make sure that the `Virus` instantiator is working.
	'''

	virus = Virus("HIV", 0.8, 0.3)
	assert virus.name == "HIV"
	assert virus.reproduction_rate == 0.8
	assert virus.mortality_rate == 0.3


# XXX TODO XXX
# Create your own tests that model other viruses.
