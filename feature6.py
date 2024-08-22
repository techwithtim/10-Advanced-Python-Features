class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Open the file
        self.file = open(self.filename, self.mode)
        print(f"Opening file {self.filename}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Close the file
        self.file.close()
        print(f"Closing file {self.filename}")
        # Handle exceptions (if any) here
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return True  # Suppress exceptions, if needed


# Using the custom context manager
if __name__ == "__main__":
    with FileManager("example.txt", "w") as file:
        file.write("Hello, world!")
        print("File written successfully")

    # If there's an exception within the 'with' block, it will be handled by __exit__.
    with FileManager("example.txt", "r") as file:
        content = file.read()
        print(f"File content: {content}")
