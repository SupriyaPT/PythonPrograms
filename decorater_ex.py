def decorator_function(function):

    def wrapper_function(*args, **kwargs):
        print("addition to existing print")
        return function(*args, **kwargs)

    return wrapper_function

@decorator_function
def display():
    print("-------decorator example---------")
@decorator_function
def display_info(name, age):
    print("name and age of the person {} and {}".format(name, age))

#display = decorator_function(display)
display()

#display_info = decorator_function(display_info)
display_info("john", 36)
