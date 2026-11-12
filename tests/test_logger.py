from logger import Logger
from population import Population
from virus import Virus


def test_logger_writes_metadata(tmp_path):
	virus = Virus("Test", 0.2, 0.1)
	population = Population(10, 0.5, 1, virus)
	logger = Logger(tmp_path / "simulation.log")

	logger.log_metadata(population, virus)

	log = (tmp_path / "simulation.log").read_text(encoding="utf-8")
	assert "Virus Name: Test" in log
	assert "Population Size: 10" in log
	assert "------ CYCLE 0 ------" in log
