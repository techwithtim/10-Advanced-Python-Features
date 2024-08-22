def demonstrate_exec():
    code = """def greet(name):
    return f"Hello, {name}!\""""

    # Execute the code string
    local_scope = {}
    exec(code, {}, local_scope)
    print(local_scope["greet"]("Alice"))


def demonstrate_eval():
    # Evaluate the expression
    expression = input("Type an expression: ")

    result = eval(expression)

    print(f"Result of eval: {result}\n")


def demonstrate_safe_eval():
    # Expression to evaluate
    expression = input("Type an expression that uses a, b and c: ")

    # Define variables for the expression
    variables = {"a": 2, "b": 3, "c": 4}

    # Evaluate the expression in the context of the provided variables
    result = eval(expression, {}, variables)

    print(f"Result of safe eval: {result}\n")


demonstrate_safe_eval()
