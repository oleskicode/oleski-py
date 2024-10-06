class Predator():
    def feed(self):
        print("Hunting...")

class Prey():
    def feed(self):
        print("Eating Grass...")

class Fish(Predator, Prey):
    pass

someFish = Fish()
someFish.feed() #output is "Hunting" Predator.feed

print(Fish.mro()) #MRO is [<class '__main__.Fish'>, <class '__main__.Predator'>, <class '__main__.Prey'>, <class 'object'>]