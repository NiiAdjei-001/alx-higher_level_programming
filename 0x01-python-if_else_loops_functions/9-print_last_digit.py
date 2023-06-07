def print_last_digit(number):
    while i < len(str):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print(f"{chr(ord(str[i]) - 32)}", end="")
        else:
            print(f"{str[i]}", end="")
        i += 1
    print()
