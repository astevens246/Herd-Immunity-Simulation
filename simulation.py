import random
import uuid
from person import Person
from logger import Logger
from virus import Virus

def generate_unique_id():
    return str(uuid.uuid4())

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.logger = Logger(file_name="simulation_log.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.newly_infected = []

    def _create_population(self):
        num_vaccinated = int(self.vacc_percentage * self.pop_size)
        num_infected = self.initial_infected
        population = []

        population.extend([Person(_id=generate_unique_id(), is_vaccinated=True) for _ in range(num_vaccinated)]) 
        population.extend([Person(_id=generate_unique_id(), is_vaccinated=False, infection=self.virus) for _ in range(num_infected)])
        population.extend([Person(_id=generate_unique_id()) for _ in range(self.pop_size - num_vaccinated - num_infected)])

        return population

    def _simulation_should_continue(self):
        for person in self.population:
            if person.is_alive and not person.is_vaccinated:
                return True
        return False

    def run(self):
        time_step_counter = 0
        should_continue = True

        while should_continue:
            time_step_counter += 1
            should_continue = self._simulation_should_continue()

            self.logger.log_starting_statistics(time_step_counter, self.pop_size, self.virus)
            self.time_step()
            self.logger.log_simulation_end(time_step_counter)

    def time_step(self):
        for person in self.population:
            if person.infection:
                for _ in range(100):
                    random_person = random.choice(self.population)
                    self.interaction(person, random_person)

        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        if random_person.is_vaccinated:
            pass
        elif random_person.infection:
            pass
        elif not random_person.is_vaccinated:
            if random.random() < self.virus.repro_rate:
                self.logger.log_interactions(infected_person, random_person)
                self.newly_infected.append(random_person)

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []

if __name__ == "__main__":
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    sim.run()
