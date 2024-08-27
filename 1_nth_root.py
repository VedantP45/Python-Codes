import math

def nth_root(number, n):
    if number < 0 and n % 2 == 0:
        raise ValueError("Cannot compute an even root of a negative number.")
    
    if number == 0:
        return 0
    
    root = number ** (1 / n)
    return round(root, 2)

x = float(input('Enter number  x: '))
y = float(input('Enter a number y: '))

print("Ans: ", nth_root(x, y))
