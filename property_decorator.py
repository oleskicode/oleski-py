class Tractor:
    def __init__(self, color):
        self.color = color
        self.wheels = 4

    @property
    def get_color(self):
        return self.color


trackie = Tractor("green")

print(
    trackie.get_color
)  # without parentheses () since get_color is a property, not a method.
