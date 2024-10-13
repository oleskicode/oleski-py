def printing_dashes(func):
    def wrapper():
        print("---beginning---")
        func()
        print("-----end-----")

    return wrapper


def printing_stars(func):
    def wrapper():
        print("***start***")
        func()
        print("***end***")

    return wrapper


@printing_dashes
@printing_stars
def say_hello():
    print("Hello")


say_hello()
