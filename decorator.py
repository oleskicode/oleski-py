def printing(func):
    def wrapper():
        print("---beginning---")
        func()
        print("-----end-----")
    return wrapper

@printing
def say_hello():
    print("Hello")

say_hello()