import math

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y
squ = lambda x: x ** 2
pow = lambda x, y: x ** y
sqrt = lambda x: math.sqrt(x)
percent = lambda x, y: (x / 100) * y
try:
    cal = input("Enter one operation from the following operations add, sub, mul, div, squ, pow, sqrt, percent: ").strip().lower()
    if cal in ['add', 'sub', 'mul', 'div', 'pow', 'percent']:
        x = float(input("Enter your first value: "))
        y = float(input("Enter your second value: "))
        if cal == 'add':
            print("Result:", add(x, y))
        elif cal == 'sub':
            print("Result:", sub(x, y))
        elif cal == 'mul':
            print("Result:", mul(x, y))
        elif cal == 'div':
            if y == 0:
                raise ZeroDivisionError("can't divides by zero")
            print("Result:", div(x, y))
        elif cal == 'pow':
            print("Result:", pow(x, y))
        else:
            print("Result:", percent(x, y))
    elif cal in ['squ', 'sqrt']:
        x = float(input("Enter your value: "))
        if cal == 'squ':
            print("Result:", squ(x))
        else:
            print("Result:", sqrt(x))
    else:
        print("Invalid option.")
except ValueError:
    print("invalid input , please enter a numric value")
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print("unexpected error occured",e)