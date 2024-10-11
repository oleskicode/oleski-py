class Animal:
    def eat(self):
        print("Animal is eating")

class Predator(Animal):
    def eat(self):
        print("This Predator is Hunting")
        
    def eat_super(self):
        super().eat()

cat = Predator()
cat.eat() #This Predator is Hunting
cat.eat_super() #Animal is eating
