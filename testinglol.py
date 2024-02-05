file = open('easymaths.txt', 'a')
for i in range(1,11):
    file.write(f'{str(i)} \n')
file.close()