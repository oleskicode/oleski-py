class Wolf:
    breeds = ["Northern", "White", "Brown", "American"]

    @staticmethod
    def is_known_breed(breed):
        if breed in Wolf.breeds:
            print(f"{breed} is a known breed")
        else:
            print(f"{breed} is not a known breed")


# Calling the static method with known and unknown breeds
Wolf.is_known_breed("Brown")  # Output: Brown is a known breed
Wolf.is_known_breed("Yellow")  # Output: Yellow is not a known breed
