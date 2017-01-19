f = open('22.txt', 'r')
data = f.readline().replace('"', '').split(',')
data.sort()


result = 0
for index, name in enumerate(data):
    index += 1

    sum = 0
    for char in name:
        sum += (ord(char)-64)
    result += sum * index

print(result)
