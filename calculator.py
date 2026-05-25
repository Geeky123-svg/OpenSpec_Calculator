from typing import Any, Dict


def parse_number(value: Any, name: str) -> float:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be a number.")

    if isinstance(value, (int, float)):
        return float(value)

    if isinstance(value, str):
        stripped = value.strip()
        if stripped == "":
            raise ValueError(f"{name} must be a number.")
        try:
            return float(stripped)
        except ValueError:
            raise ValueError(f"{name} must be a number.")

    raise ValueError(f"{name} must be a number.")


def add(a: Any, b: Any) -> float:
    return parse_number(a, "a") + parse_number(b, "b")


def subtract(a: Any, b: Any) -> float:
    return parse_number(a, "a") - parse_number(b, "b")


def multiply(a: Any, b: Any) -> float:
    return parse_number(a, "a") * parse_number(b, "b")


def divide(a: Any, b: Any) -> float:
    numerator = parse_number(a, "a")
    denominator = parse_number(b, "b")
    if denominator == 0:
        raise ValueError("Division by zero is not allowed.")
    return numerator / denominator


def calculate(operation: str, a: Any, b: Any) -> float:
    op = operation.strip().lower()
    if op == "add":
        return add(a, b)
    if op == "subtract":
        return subtract(a, b)
    if op == "multiply":
        return multiply(a, b)
    if op == "divide":
        return divide(a, b)

    raise ValueError(f"Unsupported operation: {operation}")


def build_error_response(message: str) -> Dict[str, str]:
    return {"error": message}
