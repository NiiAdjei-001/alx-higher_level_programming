#!/usr/bin/python3
def safe_print_integer_err(value):
    result = False
    try:
        print("{:d}".format(value))
        result = True
    except Exception as err:
        print(err)
        result = False
    finally:
        return result
