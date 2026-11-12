import pytest

from person import Person
from virus import Virus


def test_vacc_person_instantiation():
	# Create some people to test if our init method works as expected...
	person = Person(1, True)
	assert person._id == 1
	assert person.is_alive is True
	assert person.is_vaccinated is True
	assert person.infection is None


@pytest.mark.skip(reason="TODO: complete the assertions for an unvaccinated person.")
def test_not_vacc_person_instantiation():
	person = Person(2, False)

	# XXX TODO XXX
	# Complete your own assert statements that test the values at each attribute.
	# assert ...
	pass


@pytest.mark.skip(reason="TODO: complete the assertions for an infected person.")
def test_sick_person_instantiation():
	# Create a `Virus` object to give a `Person` object an infection.
	virus = Virus("Dysentery", 0.7, 0.2)

	# Create a `Person` object and give them the virus infection.
	person = Person(3, False, virus)

	# XXX TODO XXX
	# Complete your own assert statements that test the values at each attribute.
	# assert ...
	pass


@pytest.mark.skip(reason="TODO: complete this test for resolve_infection().")
def test_did_survive_infection():
	# XXX TODO XXX
	# Create a `Virus` object to give a `Person` object an infection.
	virus = Virus("Dysentery", 0.7, 0.2)

	# XXX TODO XXX
	# Create a `Person` object and give them the virus infection.
	person = Person(4, False, virus)

	# Resolve whether the `Person` survives the infection or not.
	survived = person.did_survive_infection()

	# Check if the `Person` survived or not.
	if survived:
		assert person.is_alive is True

		# XXX TODO XXX
		# Write your own assert statements that test the values of
		# each attribute for a `Person` who survived.
		assert False # Replace with something else.

	else:
		assert person.is_alive is False

		# XXX TODO XXX
		# Write your own assert statements that test the values of
		# each attribute for a `Person` who did not survive.
		assert False # Replace with something else.
