contents = open('meat.txt', 'r')
for i in contents:
    if 'borscht' in i:
        print(i)
contents.close()