# simulation.py

import random
import uuid
from person import Person
from virus import Virus
from logger import Logger

def generate_unique_id():
    return str(uuid.uuid4())

class Simulation:
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.population = self._create_population()
        self.newly_infected = []
        self.logger = Logger(file_name="simulation_log.txt")

    def _create_population(self):
        num_vaccinated = int(self.vacc_percentage * self.pop_size)
        num_infected = self.initial_infected
        population = []

        population.extend([Person(person_id=generate_unique_id(), is_vaccinated=True) for _ in range(num_vaccinated)])
        population.extend([Person(person_id=generate_unique_id(), is_vaccinated=False, infection=self.virus) for _ in range(num_infected)])
        population.extend([Person(person_id=generate_unique_id()) for _ in range(self.pop_size - num_vaccinated - num_infected)])

        return population

    def _simulation_should_continue(self):
        return any(person.is_alive and not person.is_vaccinated for person in self.population)

    def run(self):
        # Print the simulation log
        print(f"Population Size: {self.pop_size:,}")
        print(f"Vaccination Percentage: {self.vacc_percentage * 100}%")
        print(f"Virus Name: {self.virus.name}")
        print(f"Mortality Rate: {self.virus.mortality_rate * 100}%")
        print(f"Reproduction Rate: {self.virus.repro_rate}")
        print(f"Number of People Initially Infected: {self.initial_infected}\n")
        print("Starting the simulation...\n")

        time_step_counter = 0
        should_continue = True

        self.logger.log_introduction(self.pop_size, self.initial_infected, self.virus)

        while should_continue:
            time_step_counter += 1
            should_continue = self._simulation_should_continue()

            num_new_infections, num_deaths, current_stats = self.calculate_iteration_stats()

            self.logger.log_iteration(time_step_counter, num_new_infections, num_deaths, current_stats)
            self.time_step()

        total_living = sum(person.is_alive for person in self.population)
        total_dead = self.pop_size - total_living
        end_reason = "Simulation completed"
        interactions_stats = {
            'total': self.logger.get_total_interactions(),
            'vaccination': self.logger.get_vaccination_interactions(),
            'death': self.logger.get_death_interactions()
        }

        self.logger.log_summary(total_living, total_dead, end_reason, interactions_stats)
        self.logger.log_simulation_end(time_step_counter)

    def calculate_iteration_stats(self):
        num_new_infections = len(self.newly_infected)
        num_deaths = sum(not person.is_alive for person in self.population)
        current_stats = {
            'total_living': sum(person.is_alive for person in self.population),
            'total_dead': sum(not person.is_alive for person in self.population),
            'total_vaccinated': sum(person.is_vaccinated for person in self.population)
        }
        return num_new_infections, num_deaths, current_stats

    def time_step(self):
        new_infections = []

        for person in self.population:
            if person.is_alive and not person.is_vaccinated and person.infection:
                for _ in range(100):
                    random_person = random.choice(self.population)
                    self.interaction(person, random_person, new_infections)

        self.resolve_states(new_infections)

    def interaction(self, infected_person, random_person, new_infections):
        if (
            not random_person.is_vaccinated
            and not random_person.infection
            and random_person not in new_infections
        ):
            if random_person.is_vaccinated:
                self.logger.log_interaction(infected_person, random_person, interaction_type="vaccination")
            else:
                if not random_person.infection:
                    if random.random() < self.virus.repro_rate:
                        new_infections.append(random_person)
                        self.logger.log_interaction(infected_person, random_person, interaction_type="infection")

    def resolve_states(self, new_infections):
        for person in self.population:
            if person in new_infections:
                person.infection = self.virus
            elif person.infection:
                if random.random() < self.virus.mortality_rate:
                    person.is_alive = False
                    person.infection = None
                    self.logger.log_interaction(person, None, interaction_type="death")
                else:
                    person.is_vaccinated = True
                    person.infection = None
                    self.logger.log_interaction(person, None, interaction_type="survival")

        self.dead_people_cannot_be_infected()

    def dead_people_cannot_be_infected(self):
        for person in self.population:
            if not person.is_alive:
                person.infection = None

        self.infect_newly_infected()

    def infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []

if __name__ == "__main__":
    virus = Virus(name="ExampleVirus", repro_rate=0.2, mortality_rate=0.05)
    sim = Simulation(virus=virus, pop_size=1000, vacc_percentage=0.1, initial_infected=5)
    sim.run()
    sim.logger.close_log_file()  # Close the log file after the simulation is done