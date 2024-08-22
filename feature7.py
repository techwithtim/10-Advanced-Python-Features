class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        """
        The __iter__ method makes this class an iterable.
        It should return an iterator object.
        """
        return self

    def __next__(self):
        """
        The __next__ method defines the iteration behavior.
        It should return the next item in the sequence or raise StopIteration.
        """
        if self.current < self.end:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


# Example usage of the custom iterator
if __name__ == "__main__":
    my_range = MyRange(1, 5)  # Create an instance of MyRange

    # Iterating over the custom iterator using a for loop
    for number in my_range:
        print(number)  # Output: 1, 2, 3, 4
