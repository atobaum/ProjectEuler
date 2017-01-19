f = open('18.txt', 'r')
data = [];
for line in f:
    data.append([int(x) for x in line.rstrip().split(' ')])

data.reverse()

for i in range(len(data)-1):
    line = data[i]
    for j in range(len(line)-1):
        data[i+1][j] += max(line[j], line[j+1])


print("The answer is ", data[len(data)-1][0]) #result
