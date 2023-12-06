class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your your virus
        self.name = name
        # TODO Define the other attributes of Virus
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate
        


# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    # Add two more tests with different instances
    virus2 = Virus("Influenza", 0.5, 0.1)
    assert virus2.name == "Influenza"
    assert virus2.repro_rate == 0.5
    assert virus2.mortality_rate == 0.1

    virus3 = Virus("COVID-19", 0.7, 0.2)
    assert virus3.name == "COVID-19"
    assert virus3.repro_rate == 0.7
    assert virus3.mortality_rate == 0.2