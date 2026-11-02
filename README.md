# Herd Immunity Simulation
This project simulates *Herd Immunity*, modeling how a virus moves through a population where some (but not all) of a population is vaccinated against the virus.

> #### Nolt's Note
> This project template was originally created in 2018/2019, before the COVID-19 pandemic.
> At that point I was studying at Make School, and I completed this project as a part of my education.
> Since then, the project aged quite well; the project is even more fitting to learn with, thanks to some serious retrospective.
> I revisited the project in 2025/2026, just to polish it up in my projects portfolio.
>
> If you are interested in forking this project to work on yourself, feel free to [Fork the Template Repository](https://github.com/remake-school/cs-101-project-herd-immunity-simulation)!

## Getting Started
### Running the App
1. *Fork* or *Clone* this repository into a local directory of your choice.
	- For example, you could run `git clone https://github.com/noltron000/herd-immunity`.
1. Navigate into the root of the directory with your terminal.
	- Use the `cd` command to get there.
1. Run the app with `python3 simulation.py`.
	- While you can provide command-line arguments, running the app with no arguments will make the app default to using *Ebola* virus data, with a preset population size.
	- You will see the output in your terminal.
		It will also generate a text logfile (although its contents may be exactly the same as the included textfile, so no perceivable file changes may occur).

#### Customizing Inputs
By default, this project runs a simulation of Ebola, set up as a default at the end of `simulation.py`.
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
> `python3 simulation.py <virus_name> <reproduction_rate> <mortality_rate> <population_size> <vaccination_rate> <OPTIONAL: initial_infections>`

Here is an example to use:
> `python3 simulation.py COVID 0.30 0.30 10000 0.00 10`

### Terminology
TODO: Discuss statistics of viral infections throuhgout populations here. It's like actuary science!
