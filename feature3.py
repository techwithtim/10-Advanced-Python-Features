# Variable Annotations
name: str = "Alice"
age: int = 30
is_student: bool = False


# Function Annotations
def greet(person: str, age: int) -> str:
    """
    Greets a person by name and age.

    :param person: The name of the person (expected to be a string).
    :param age: The age of the person (expected to be an integer).
    :return: A greeting message (expected to be a string).
    """
    return f"Hello, {person}! You are {age} years old."


# Using the function
greeting_message = greet(name, age)
print(greeting_message)

# Showing annotations
print("\nFunction Annotations:", greet.__annotations__)
print("Variable Annotations:", __annotations__)
