import datetime

class Logger:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None  # Add this line to initialize the file attribute

        self.log_file = open(self.file_name, 'w')
        self.vaccination_interactions = 0
        self.death_interactions = 0
        
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

    def log_summary(self, total_living, total_dead, end_reason, interactions_stats):
        # Log a summary of the simulation
        self.file.write("\n\nSimulation Summary\n")
        self.file.write("-------------------\n")
        self.file.write(f"Total living: {total_living}\n")
        self.file.write(f"Total dead: {total_dead}\n")
        self.file.write(f"End reason: {end_reason}\n")
        self.file.write("\nInteractions Stats:\n")
        self.file.write(f"Total interactions: {interactions_stats['total']}\n")
        self.file.write(f"Vaccination interactions: {interactions_stats['vaccination']}\n")
        self.file.write(f"Death interactions: {interactions_stats['death']}\n")

    def log_starting_statistics(self, time_step_counter, pop_size, virus):
        with open(self.file_name, 'a') as file:
            file.write(f"Start of Simulation - Time Step: {time_step_counter}\n")
            file.write(f"Initial Population Size: {pop_size}\n")
            file.write(f"Virus Information: {virus.name}, Repro Rate: {virus.repro_rate}, Mortality Rate: {virus.mortality_rate}\n")
            file.write("\n")


    def log_interaction(self, person1, person2, interaction_type):
        with open(self.file_name, 'a') as file:
            if person2 is not None:
                file.write(f"{person1._id}\t{person2._id}\t1\n")  # Assuming 1 interaction
            else:
                file.write(f"{person1._id}\tNone\t{interaction_type}\n")  # Log the interaction type for the end of simulation

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
    def get_total_interactions(self):
            # Return the total number of interactions
            return self.vaccination_interactions + self.death_interactions
    def get_vaccination_interactions(self):
        return self.vaccination_interactions

    def get_death_interactions(self):
        return self.death_interactions

    def close_log_file(self):
        self.log_file.close()