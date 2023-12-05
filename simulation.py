import sys
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

        self.logger.log_introduction(self.pop_size, self.initial_infected, self.virus)

        while should_continue:
            time_step_counter += 1
            should_continue = self._simulation_should_continue()

            self.logger.log_iteration(time_step_counter, num_new_infections, num_deaths, current_stats)
            self.time_step()

        total_living = sum(person.is_alive for person in self.population)
        total_dead = self.pop_size - total_living
        interactions_stats = {
            'total': total_interactions,
            'vaccination': num_vaccination_interactions,
            'death': num_death_interactions
        }
        self.logger.log_summary(total_living, total_dead, num_vaccinations, end_reason, interactions_stats)
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
    # Parse command-line arguments
    if len(sys.argv) != 7:
        print("Usage: python3 simulation.py <population size> <vacc_percentage> <virus_name> <mortality_rate> <repro_rate> <initial_infected>")
        sys.exit(1)

    pop_size = int(sys.argv[1])
    vacc_percentage = float(sys.argv[2])
    virus_name = sys.argv[3]
    mortality_rate = float(sys.argv[4])
    repro_rate = float(sys.argv[5])
    initial_infected = int(sys.argv[6])

    # Create Virus instance
    virus = Virus(virus_name, repro_rate, mortality_rate)

    # Create Simulation instance
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    # Run the simulation
    sim.run()
