import datetime

class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name
        with open(self.file_name, 'w') as log_file:
            log_file.write("Simulation Log\n")

    def log_introduction(self, pop_size, initial_infected, virus):
        with open(self.file_name, 'a') as file:
            file.write("Before Simulation Begins: Display Introduction\n")
            file.write(f"Initial size of the population: {pop_size}\n")
            file.write(f"Initial number of infected people: {initial_infected}\n")
            file.write(f"Name of the virus: {virus.name}\n")
            file.write(f"Stats for the virus: Repro Rate - {virus.repro_rate}, Mortality Rate - {virus.mortality_rate}\n")
            file.write(f"Date the simulation was run: {datetime.datetime.now()}\n")
            file.write("\n")

    def log_iteration(self, step_number, new_infections, deaths, current_stats):
        with open(self.file_name, 'a') as file:
            file.write(f"While Simulation Runs: Display Every Iteration\n")
            file.write(f"Step: {step_number}\n")
            file.write(f"The number of new infections: {new_infections}\n")
            file.write(f"The number of deaths: {deaths}\n")
            file.write("Statistics for the current state of the population:\n")
            file.write(f"Total number of living people: {current_stats['total_living']}\n")
            file.write(f"Total number of dead people: {current_stats['total_dead']}\n")
            file.write(f"Total number of vaccinated people: {current_stats['total_vaccinated']}\n")
            file.write("\n")

    def log_summary(self, total_living, total_dead, num_vaccinations, end_reason, interactions_stats):
        with open(self.file_name, 'a') as file:
            file.write("After Simulation Ends: Summary\n")
            file.write(f"Total living: {total_living}\n")
            file.write(f"Total dead: {total_dead}\n")
            file.write(f"Number of vaccinations: {num_vaccinations}\n")
            file.write(f"Why the simulation ended: {end_reason}\n")
            file.write(f"Total number of interactions that happened in the simulation: {interactions_stats['total']}\n")
            file.write(f"Number of interactions that resulted in vaccination: {interactions_stats['vaccination']}\n")
            file.write(f"Number of interactions that resulted in death: {interactions_stats['death']}\n")

    def log_starting_statistics(self, time_step_counter, pop_size, virus):
        with open(self.file_name, 'a') as file:
            file.write(f"Start of Simulation - Time Step: {time_step_counter}\n")
            file.write(f"Initial Population Size: {pop_size}\n")
            file.write(f"Virus Information: {virus.name}, Repro Rate: {virus.repro_rate}, Mortality Rate: {virus.mortality_rate}\n")
            file.write("\n")

    def log_interactions(self, infected_person, random_person):
        with open(self.file_name, 'a') as file:
            file.write(f"{infected_person._id}\t{random_person._id}\t1\n")  # Assuming 1 interaction

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        with open(self.file_name, 'a') as file:
            file.write(f"{step_number}\t{population_count}\t{number_of_new_fatalities}\n")

    def log_time_step(self, time_step_number):
        with open(self.file_name, 'a') as file:
            file.write(f"{time_step_number}\n")

    def log_simulation_end(self, time_step_counter):
        with open(self.file_name, 'a') as file:
            file.write(f"End of Simulation - Time Step: {time_step_counter}\n")
            file.write("Simulation Ended\n")
