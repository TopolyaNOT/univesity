from typing import Any

def to_str(a: Any) -> str:
    try:
        return str(a)
    except Exception as e:
        return f"Error: {e}"
    

def to_int(a: Any) -> int | str:
    try:
        return int(a)
    except Exception as e:
        return f"Error: {e}"


def to_float(a: Any) -> float | str:
    try:
        return float(a)
    except Exception as e:
        return f"Error: {e}"


def to_bool(a: Any) -> bool | str:
    try:
        return bool(a)
    except Exception as e:
        return f"Error: {e}"


def to_list(a: Any) -> list | str:
    try:   
        return list(a)
    except Exception as e:
        return f"Error: {e}"


def to_tuple(a: Any) -> tuple | str:
    try:
        if isinstance(a, (str, bytes, bytearray)):
            return tuple(a)
        return tuple(a)
    except Exception as e:
        return f"Error: {e}"


def to_set(a: Any) -> set | str:
    try:
        return set(a)
    except Exception as e:
        return f"Error: {e}"


def to_dict(a: Any) -> dict | str:
    try:
        return dict(a)
    except Exception as e:
        return f"Error: {e}"