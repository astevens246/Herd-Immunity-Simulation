import random
from virus import Virus

class Person(object):
    # Define a person.
    def __init__(self, _id, is_vaccinated=False, infection=None):
        # A person has an id, is_vaccinated, and possibly an infection
        self._id = _id  # int
        # TODO: Define the other attributes of a person here
        self.is_vaccinated = is_vaccinated  # boolean
        self.infection = infection  # virus object
        self.is_alive = True

    def die(self):
        self.is_alive = False

    def did_survive_infection(self):
        # This method checks if a person survived an infection.
        # TODO: Only called if the infection attribute is not None.
        if self.infection:
            # Check generate a random number between 0.0 - 1.0
            # If the number is less than the mortality rate of the
            # person's infection, they have passed away.
            # Otherwise, they have survived infection, and they are now vaccinated.
            # Set their properties to show this
            survived = random.random() > self.infection.mortality_rate
            if survived:
                self.is_vaccinated = True  # person is now vaccinated
            return survived
        else:
            return False  # Return False if there's no infection

if __name__ == "__main__":
    # This section is incomplete, finish it, and use it to test your Person class
    # TODO: Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    # TODO: Test unvaccinated_person's attributes here...
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    # TODO: complete your own assert statements that test
    # the values of each attribute
    # assert ...
    assert infected_person._id == 3
    assert infected_person.is_vaccinated is False
    assert infected_person.infection == virus

    # Now that you have a list of 100 people. Resolve whether the Person
    # survives the infection or not by looping over the people list.
    # Create a list to hold 100 people. Use the loop below to make 100 people
    def create_people():
        people = []
        for i in range(1, 100):
            # TODO: Make a person with an infection
            # create a virus object to give a person an infection
            virus = Virus("Dysentery", 0.7, 0.2)
            # create a person object and give them the virus infection
            person = Person(_id=i, is_vaccinated=False, infection=virus)
            # TODO: Append the person to the people list
            people.append(person)
        return people

    # Use the static method to create a list of people
    people = create_people()

    # Now you can use the created list of people in your simulation
    for person in people:
        # For each person call that person's did_survive_infection method
        survived = person.did_survive_infection()

    # Count the people that survived and did not survive:
    did_survive = sum(person.is_alive for person in people)
    did_not_survive = 100 - did_survive

    # Loop over all of the people
    for person in people:
        survived = person.did_survive_infection()
        # If a person is_alive True add one to did_survive
        if person.is_alive:
            did_survive += 1
        # If a person is_alive False add one to did_not_survive
        else:
            did_not_survive += 1

    # When the loop is complete print your results.
    print(f"{did_survive} people survived and {did_not_survive} did not survive.")

    # The results should roughly match the mortality rate of the virus
    # For example, if the mortality rate is 0.2 roughly 20% of the people
    # should succumb.
