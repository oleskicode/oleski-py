from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod  # main line here
    def drive(self):
        print("Vehicle moving...")

class Tractor(Vehicle):
    def drive(self):
        print("Tractor moving...")

green_tractor = Tractor()
green_tractor.drive()

# theoretical_vehicle = Vehicle()
# theoretical_vehicle.drive()
