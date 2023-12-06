import unittest
from simulation import Simulation
from virus import Virus

class TestSimulation(unittest.TestCase):
    def setUp(self):
        # Set up any initial configurations or objects needed for the tests
        self.virus = Virus(name="TestVirus", repro_rate=0.5, mortality_rate=0.1)

    def test_simulation_creation(self):
        # Test if the simulation is created successfully
        sim = Simulation(virus=self.virus, pop_size=100, vacc_percentage=0.2, initial_infected=5)
        self.assertIsInstance(sim, Simulation)

    def test_simulation_run(self):
        # Test if the simulation runs without errors
        sim = Simulation(virus=self.virus, pop_size=100, vacc_percentage=0.2, initial_infected=5)
        sim.run()

        # Add more specific assertions based on your requirements

if __name__ == '__main__':
    unittest.main()
