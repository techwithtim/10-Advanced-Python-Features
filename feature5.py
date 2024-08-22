def my_decorator(func):
    """
    A simple decorator that prints a message before and after the execution of the function.
    """

    def wrapper(*args, **kwargs):
        print("Before the function execution.")
        result = func(*args, **kwargs)
        print("After the function execution.")
        return result

    return wrapper


@my_decorator
def say_hello(name):
    """
    A simple function that greets the user.
    """
    print(f"Hello, {name}!")


if __name__ == "__main__":
    # Example 1: Using the decorator with the say_hello function
    say_hello("Alice")
