import random
def get_random_list(pNumber):
    numbers = []
    for i in range(1, pNumber+1):
        numbers.append(random.randint(1, 100))
    return numbers

def evenMean(pList):
    even_numbers = []
    for i in pList:
        if i % 2 == 0:
            even_numbers.append(i)
    return f"{sum(even_numbers)/len(even_numbers):.3f}"

res = get_random_list(random.randint(1, 100))
print(evenMean(res))