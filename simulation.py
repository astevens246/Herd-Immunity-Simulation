import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.logger = Logger()
        # TODO: Store the virus in an attribute
        self.virus = virus
        # TODO: Store pop_size in an attribute
        self.pop_size = pop_size
        # TODO: Store the vacc_percentage in a variable
        self.vacc_percentage = vacc_percentage
        # TODO: Store initial_infected in a variable
        self.initial_infected = initial_infected
        # You need to store a list of people (Person instances)
        # Some of these people will be infected some will not. 
        # Use the _create_population() method to create the list and 
        # return it storing it in an attribute here. 
        self.population = self._create_population()
        
        # TODO: Call self._create_population() and pass in the correct parameters.
        self._create_population()             

    def _create_population(self):
        # TODO: Create a list of people (Person instances). This list 
        # should have a total number of people equal to the pop_size. 
        # Some of these people will be uninfected and some will be infected.
        # The number of infected people should be equal to the initial_infected
        num_vaccinated = int(self.vacc_percentage * self.pop_size)
        num_infected = self.initial_infected
        # Create a list to store the population
        population = []
        # Create vaccinated indivituals
        population.extend([Person(is_vaccinated=True) for _ in range(num_vaccinated)]) 
        # Create infected indivituals
        population.extend([Person(infection=self.virus) for _ in range(num_infected)])
        
        # Create healthy individuals
        population.extend([Person() for _ in range(self.pop_size - num_vaccinated - num_infected)])
        # TODO: Return the list of people
        return population

    def _simulation_should_continue(self):
        # This method will return a boolean indicating if the simulation 
        # should continue. 
        # The simulation should not continue if all of the people are dead, 
        # or if all of the living people have been vaccinated. 
        # TODO: Loop over the list of people in the population. Return True
        # if the simulation should continue or False if not.
        for person in self.population:
            if person.is_alive() and not person.is_vaccinated:
                return True
            return False

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 

        time_step_counter = 0
        should_continue = True

        while should_continue:
            # TODO: Increment the time_step_counter
            time_step_counter += 1
            # TODO: for every iteration of this loop, call self.time_step() 
            # Call the _simulation_should_continue method to determine if 
            # the simulation should continue
            should_continue = self._simulation_should_continue()
            

        # TODO: Write meta data to the logger. This should be starting 
        # statistics for the simulation. It should include the initial
        # population size and the virus. 
            self.logger.log_starting_statistics(time_step_counter, self.pop_size, self.virus)
        
        # TODO: When the simulation completes you should conclude this with 
        # the logger. Send the final data to the logger. 
            self.logger.log_simulation_end(time_step_counter)

    def time_step(self):
        # This method will simulate interactions between people, calulate 
        # new infections, and determine if vaccinations and fatalities from infections
        # The goal here is have each infected person interact with a number of other 
        # people in the population
        # TODO: Loop over your population
        # For each person if that person is infected
        # have that person interact with 100 other living people 
        # Run interactions by calling the interaction method below. That method
        # takes the infected person and a random person
        for person in self.population:
            if person.infection:
                for _ in range(100):
                    random_person = random.choice(self.population)
                    self.interaction(person, random_person)
         # infect newly infected people at the end of the time step.
        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        # TODO: Finish this method.
        # The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0.0 and 1.0.  If that number is smaller
            #     than repro_rate, add that person to the newly infected array
            #     Simulation object's newly_infected array, so that their infected
            #     attribute can be changed to True at the end of the time step.
        if random_person.is_vaccinated:
            # nothing happens to vaccinated person
            pass
        elif random_person.is_infected:
            # nothing happens to infected person
            pass
        elif not random_person.is_vaccinated:
            # if the random person is unvaccinated and uninfected, determine if they get infected
            if random.random() < self.virus.repro_rate:
                self.logger.log_interaction(infected_person, random_person)
                self.population.append(random_person)
        # TODO: Call logger method during this method.
        pass

    def _infect_newly_infected(self):
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass


if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the imulation
    virus = Virus(virus, pop_size, vacc_percentage, initial_infected)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    # sim.run()
    sim.run()
