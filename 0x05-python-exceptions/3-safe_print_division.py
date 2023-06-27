#!/usr/bin/python3
def safe_print_division(a, b):
    """My Safe Print division function

    Args:
        a: numerator integer
        b: denominator integer

    Returns:
        The returns the value of math operation a/b
    """
    result = 0
    try:
        result = a / b
        return result
    except Exception:
        result = None
        return result
    finally:
        print("Inside result: {}".format(result))
