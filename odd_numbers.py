import random

def checkNum(number):
    file = open('oddNumbers.txt', 'a')
    count = 0
    for i in range(1, number+1):
        count += 1
        if i % 2 == 0:
            file.write(f'Digit {i} is even \n')
        else:
            file.write(f'Digit {i} is odd \n')
    file.close()
    print(count)
checkNum(1000)
