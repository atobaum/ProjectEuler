
def sumOfDivisors(n):
    sum = 0
    for i in range(1,n):
        if(n%i == 0):
            sum += i

    return sum

def isAmicable(a):
    b = sumOfDivisors(a)
    if(a==b):
        return False
    if(a == sumOfDivisors(b)):
        return True
    else:
        return False

sum = 0
for n in range(10000):
    if(isAmicable(n)):
        print(n, "is amicable number")
        sum += n
print(sum)
