from strands import tool


@tool
def calculate(expression: str) -> str:
    """Evaluate a simple mathematical expression.

    Args:
        expression: A mathematical expression to evaluate (e.g., '2 + 3 * 4').

    Returns:
        The result of the expression as a string, or an error message.
    """
    allowed_chars = set("0123456789+-*/(). ")
    if not all(c in allowed_chars for c in expression):
        return f"Error: Expression contains invalid characters: {expression}"

    try:
        result = eval(expression)  # noqa: S307
        return f"{expression} = {result}"
    except (SyntaxError, ZeroDivisionError, TypeError, NameError) as e:
        return f"Error evaluating '{expression}': {e}"
