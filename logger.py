class Logger(object):
    def __init__(self, file_name):
        # Initialize the Logger with the given file_name
        self.file_name = file_name
        # Open the file in 'w' mode to overwrite existing content or create a new file
        with open(self.file_name, 'w') as log_file:
            log_file.write("Simulation Log\n")  # Add any initial information to the log file

    def log_starting_statistics(self, time_step_counter, pop_size, virus):
        # Log starting statistics to the file.
        # Include the initial population size and virus information.
        with open(self.file_name, 'a') as file:
            file.write(f"Start of Simulation - Time Step: {time_step_counter}\n")
            file.write(f"Initial Population Size: {pop_size}\n")
            file.write(f"Virus Information: {virus.name}, Repro Rate: {virus.repro_rate}, Mortality Rate: {virus.mortality_rate}\n")
            file.write("\n")

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        # Log interactions at each step with the number of interactions and new infections
        with open(self.file_name, 'a') as file:
            file.write(f"{step_number}\t{number_of_interactions}\t{number_of_new_infections}\n")

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        # Log infection survival information
        with open(self.file_name, 'a') as file:
            file.write(f"{step_number}\t{population_count}\t{number_of_new_fatalities}\n")

    def log_time_step(self, time_step_number):
        # Log the time step number
        with open(self.file_name, 'a') as file:
            file.write(f"{time_step_number}\n")

    def log_simulation_end(self, time_step_counter):
        # Log the end of the simulation
        with open(self.file_name, 'a') as file:
            file.write(f"End of Simulation - Time Step: {time_step_counter}\n")
            file.write("Simulation Ended\n")
