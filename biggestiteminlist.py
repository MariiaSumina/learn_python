"""
Дополните приведенный код, используя цикл for и встроенную функцию max(), чтобы он выводил максимальный элемент среди всех элементов вложенных списков списка list1.

list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

ответ должен быть одна максимальная цифра.
"""
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
bigestnum = []
for i in list1:
    bignum = max(i)
    bigestnum.append(bignum)

print(max(bigestnum))