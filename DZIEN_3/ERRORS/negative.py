class NegativeNumberError(Exception):
    pass

def square_root(x):
    if x < 0:
        raise NegativeNumberError("Square root of negative number is not defined")
    return x ** 0.5

try:
    number = float(input("Enter a number: "))
    result = square_root(number)
    print(f"The square root of {number} is {result}")
except NegativeNumberError as e:
    print(e)
