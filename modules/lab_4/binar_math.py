from typing import Any

def add(a: Any, b: Any) -> str:
    try:
        result = f"result: {a} + {b} = {a + b} \n rtype: {type(a+b)}  \n"
        return result
    except Exception as e:
        return f"Error: {e}"


def subtract(a: Any, b: Any) -> str:
    try:
        result = f"result: {a} - {b} = {a - b} \n rtype: {type(a - b)} \n"
        return result
    except Exception as e:
        return f"Error: {e}"


def multiply(a: Any, b: Any) -> str:
    try:

        result = f"result: {a} * {b} = {a * b} \n rtype: {type(a * b)} \n"
        return result
    except Exception as e:
        return f"Error: {e}"


def divide(a: Any, b: Any) -> str:
    try:
        result = f"result: {a} / {b} = {a / b} \n rtype: {type(a / b)} \n"
        return result
    except Exception as e:
        return f"Error: {e}"