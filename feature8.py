def count_up_to(max_value):
    """
    A generator function that yields numbers from 1 up to max_value.
    """
    current = 1
    while current <= max_value:
        yield current  # Yield the current value and pause execution
        current += 1  # Increment the current value


if __name__ == "__main__":
    counter = count_up_to(10000000)

    for number in counter:
        print(number)
