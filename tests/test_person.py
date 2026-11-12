from person import Person
from virus import Virus


def test_vacc_person_instantiation():
	# Create some people to test if our init method works as expected...
	person = Person(1, True)
	assert person._id == 1
	assert person.is_alive is True
	assert person.is_vaccinated is True
	assert person.infection is None


def test_not_vacc_person_instantiation():
	person = Person(2, False)

	assert person._id == 2
	assert person.is_alive is True
	assert person.is_vaccinated is False
	assert person.infection is None
	assert person.is_infected is False


def test_sick_person_instantiation():
	virus = Virus("Dysentery", 0.7, 0.2)
	person = Person(3, False, virus)

	assert person._id == 3
	assert person.is_alive is True
	assert person.is_vaccinated is False
	assert person.infection is virus
	assert person.is_infected is True


def test_did_survive_infection(monkeypatch):
	virus = Virus("Dysentery", 0.7, 0.2)
	survivor = Person(4, False, virus)
	deceased = Person(5, False, virus)

	# Set deterministic rolls to check both possible outcomes.
	rolls = iter((0.9, 0.1))
	monkeypatch.setattr("person.random.random", lambda: next(rolls))

	assert survivor.resolve_infection() is True
	assert survivor.is_alive is True
	assert survivor.is_vaccinated is True
	assert survivor.infection is None

	assert deceased.resolve_infection() is False
	assert deceased.is_alive is False
	assert deceased.is_vaccinated is False
	assert deceased.infection is None
