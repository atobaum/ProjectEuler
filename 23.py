#Non-abundant sums
import lib
def isSumOfTwoAbundants(num):
    for n in abundant:
        if((num - n) in abundant):
            return True
        else:
            return False


abundant = [] # list for abundant numbers

for n in range(2, 28124):
    if(lib.sumOfDivisors(n) > n):
        abundant.append(n)


result = 0
for n in range(2, 28124):
    if(not isSumOfTwoAbundants(n)):
        result += n
        print (n)

print(result)
