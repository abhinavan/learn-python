class Vehicle:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels


class Car(Vehicle):
    def __init__(self, number_of_wheels):
        super().__init__(number_of_wheels)


vehicle = Vehicle(4)
print(vehicle.number_of_wheels)
