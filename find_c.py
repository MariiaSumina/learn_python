import math
a = int(input("Please enter side A: "))
b = int(input("Please enter side B: "))

if a > 0 and b > 0:
    #res = (a**2 + b**2)**(1/2)
    res = math.sqrt(a**2 + b**2)
    print(f'{res:.3f}')
else:
    print(f"Input is invalid, {a} or {b} are invalid")