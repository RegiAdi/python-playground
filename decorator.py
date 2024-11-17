# Definition of a simple decorator

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Applying the decorator using the @ syntax
@my_decorator
def say_hello():
    print("Hello!")

say_hello()

