"""
#5
Дополните приведенный код так, чтобы он выводил единственное число: сумму всех чисел списка list1, разделённую на общее количество всех чисел.

list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0

answ = 44.89473684210526
"""
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for i in list1:
    counter = counter + len(i)
for i in list1:
    for u in i:
        total = total + u
print(total/counter)