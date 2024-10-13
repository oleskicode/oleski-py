class Wolf:
    wolf_counter = 0

    def __init__(self):
        self.number = Wolf.wolf_counter  # assign number to wolf
        Wolf.wolf_counter += 1  # update total wolf counter

    @classmethod
    def how_many_wolfs(cls):
        return cls.wolf_counter


wolf1 = Wolf()
wolf2 = Wolf()

print(Wolf.how_many_wolfs())
