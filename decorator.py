# Definition of a simple decorator

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")

        func()

        print("Something is happening after the function is called.")
        print("Something is happening after the function is called.")
    return wrapper

def get(func):
    def get_decorator():
        print("start get decorator")

        func()

        print("end get decorator")
    return get_decorator

# Applying the decorator using the @ syntax
@my_decorator
def say_hello():
    print("Hello!")
    print("World!")

@get
def get_user():
    print("get_user()")

say_hello()
get_user()

