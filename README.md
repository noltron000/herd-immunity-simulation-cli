# Herd Immunity Simulation
This project simulates *Herd Immunity*, modeling how a virus moves through a population where some (but not all) of a population is vaccinated against the virus.

> #### Nolt's Note
> This project template was originally created in 2018/2019, before the COVID-19 pandemic.
> At that point, I was studying at Make School; I completed this project as a part of my education.
> Since then, the project aged quite well.
> The project is even more fitting to learn with, thanks to some serious retrospective.
> I revisited the project in 2025/2026, just to polish it up in my projects portfolio.
>
> If you are interested in forking this project to work on yourself, feel free to
> [Fork the Template Repository](https://github.com/remake-school/cs-101-project-herd-immunity-simulation)!

## How it Works
First, this project generates a population from [the `Population` class](./src/population.py).
The `__init__` method there creates a large number of people using [the `Person` class](./src/person.py), and seeds infections/vaccinations randomly.

From there, various functions from [the `Simulation` class](./src/simulation.py) do the heavy lifting.
In particular, you could check out out the methods `run()`, `cycle_step()`, and `interaction()`.

## Running the App
1. *Fork* or *Clone* this repository into a local directory of your choice.
	For example, you could run:
	~~~bash
	git clone https://github.com/noltron000/herd-immunity
	~~~
1. Navigate into the root of the directory with your terminal.
	- Use the `cd` command to get there.
1. Run the app with:
	~~~bash
 	python3 src/simulation.py
	~~~
	- While you can provide command-line arguments, running the app with no arguments will make the app default to using *Ebola* virus data, with a preset population size.
	- You will see the output in your terminal. It will also generate a text logfile (although its contents may be exactly the same as the included textfile, so no perceivable file changes may occur).

### Customizing Inputs
By default, this project runs a simulation of Ebola, set up as a default at the end of `src/simulation.py`.
That uses the following parameters:

|                              |         |
| ---------------------------- | ------- |
| Virus Name                   | Ebola   |
| Reproduction Rate            | 25%     |
| Mortality Rate               | 70%     |
| Population Size              | 100,000 |
| Vaccination Rate             | 90%     |
| Initial Number of Infections | 10      |

You can customize the parameters in the command line using the following arguments:
~~~bash
python3 src/simulation.py {VIRUS_NAME} {REPRODUCTION_RATE} {MORTALITY_RATE} {POPULATION_SIZE} {VACCINATION_RATE} {INITIAL_INFECTIONS}
~~~

Replace each `{...}` placeholder with your input; omit `{INITIAL_INFECTIONS}` if you don't want to provide that optional value.

Here is an example to use:
~~~bash
python3 src/simulation.py COVID 0.30 0.30 10000 0.00 10
~~~

## Running Tests
Install the project's test dependencies, then run the suite from the repository root:
~~~bash
python -m pip install -e ".[test]"
python -m pytest
~~~
