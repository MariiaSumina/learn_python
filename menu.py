menu_items = [
    ["sausage", 10, False],
    ["borscht", 15, False],
    ["apple", 5, True],
    ["avacado", 55, True],
    ["sandwich", 33, False]
]
#creating files
m = open('meat.txt', 'w')
v = open('vegetarians.txt', 'a')

for item in menu_items:
    name, price, check = item
    if check:
        v.write(f'{name}, {price} \n')
    else:
        m.write(f'{name}, {price} \n')

#closing files
m.close()
v.close()

print("Work is done")