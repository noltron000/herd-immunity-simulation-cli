from population import Population
from virus import Virus

################
# Logger Class #
################

class Logger:
	'''Utility class responsible for logging simulation interactions to a file.'''

	@staticmethod
	def generate_file_name(population: Population, virus: Virus):
		'''
		This static method generates a logfile name and returns it,
		based on a few parameters about the simulation (as listed).
		'''

		name = (
			f"sim_{virus.name}_"
			f"pop_{population.size}_"
			f"vac_{population.vaccination_rate}_"
			f"inf_{population.initial_infections}.txt"
		)

		return name.lower()

	def __init__(self, file_name):
		'''
		Initializes a new Logger class instance.
		The `file_name` property that's passed in should be the full name
		of the file that the logs will be written to.
		'''

		self.file_name = file_name # type: str

		print() # Add some space for legibility within the terminal.

		# XXX NOTE XXX
		# Use 'w' mode when you open the file to overwrite the old data with the new.
		# For all other methods, use the 'a' mode to append a new log to the end.
		with open(self.file_name, "w") as logfile:
			logfile.truncate()

	def write(self, content: str, verbose = True):
		'''Writes the given content to the logfile.'''
		# Print the given content to console if `verbose = true`.
		if verbose: print(content)

		# XXX NOTE XXX
		# Use 'a' mode to append content to the logfile.
		with open(self.file_name, "a") as logfile:
			# Write the given content...
			logfile.write(content)
			logfile.write("\n") # This newline helps emulate the behavior of print statements.

	def log_metadata(self, population: Population, virus: Virus):
		'''
		The simulation class should use this method immediately to log
		the specific parameters of the simulation as the first line of the file.
		'''

		# XXX TODO XXX
		# The basic header information is pretty bare-bones for now.
		# I can't really think of anything else that would need to go here.
		# Maybe an author field and a creation timestamp?
		content = (
			"====== HERD IMMUNITY SIMULATION ======\n"
			f"Virus Name: {virus.name}\n"
		)
		self.write(content)

		# XXX NOTE XXX
		# We will want to log "Cycle Zero" right away as part of initialization.
		# This shows a summary of some important data cleanly, before anyone dies.
		self.log_cycle(
			num_cycles = 0,
			num_new_infections = population.initial_infections,
			num_newly_immune = 0,
			num_new_deaths = 0,
			total_alive = population.size,
			total_deaths = 0,
			total_immune = population.initial_vaccinations,
		)

	def log_interaction(
			self,

			# XXX HINT XXX
			# The `person` parameter is usually sick.
			person,

			# XXX HINT XXX
			# Think about whether these `random_person` was sick or healthy,
			# and whether or not they were vaccinated.
			random_person,

			# XXX HINT XXX
			# This is just a logger function,
			# we don't have logic to decide whether or not infections happen here.
			did_infect=None,
		):
		'''
		The Simulation object should use this method to log
		every interaction during each time step.

		The format of the log should be:
			`"{person.ID} infects {random_person.ID}.\\n"`

		...or the other edge cases:
			`"{person.ID} didn't infect {random_person.ID}
			because {ex. 'vaccinated' or 'already sick'}.\\n"`
		'''

		if not person.is_infected:
			content = (
				f"{person._id} and {random_person._id} interacted; "
				"neither was infected."
			)
		elif did_infect:
			content = f"{person._id} infects {random_person._id}."
		elif random_person.is_infected:
			content = (
				f"{person._id} didn't infect {random_person._id} "
				"because they were already sick."
			)
		elif random_person.is_vaccinated:
			content = (
				f"{person._id} didn't infect {random_person._id} "
				"because they were vaccinated."
			)
		else:
			content = f"{person._id} didn't infect {random_person._id}."

		self.write(content, verbose=False)

	def log_infection_survival(self, person, did_die_from_infection):
		'''
		The Simulation object uses this method to log the results of every call of
		a Person object's `.resolve_infection()` method.

		The format of the log should be:
			`"{person.ID} died from infection.\\n"
			or "{person.ID} survived infection.\\n"`
		'''

		if did_die_from_infection:
			content = f"{person._id} died from infection."
		else:
			content = f"{person._id} survived infection."

		self.write(content, verbose=False)

	def log_cycle(
			self,
			num_cycles,
			num_new_infections: int,
			num_newly_immune: int,
			num_new_deaths: int,
			total_alive: int,
			total_immune: int,
			total_deaths: int,
		):
		'''This writes summary statistics to the logfile.'''

		logs = (
			f"------ CYCLE {num_cycles} ------\n"
			f"   new cases: {num_new_infections}\n"
			f"newly immune: {num_newly_immune}\n"
			f"  new deaths: {num_new_deaths}\n"
			f" total alive: {total_alive}\n"
			f"total immune: {total_immune}\n"
			f"total deaths: {total_deaths}\n"
		)
		self.write(logs)
