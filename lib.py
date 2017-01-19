primes = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23, 29]

def primeFacorization(n):
    primeDivisors = {}
    while True:
        if n==1:
            return primeDivisors #finish prime factorization.

        for i in range(len(primes)):
            prime = primes[i]
            if n%prime == 0:
                if prime in primeDivisors.keys():
                    primeDivisors[prime] += 1
                else:
                    primeDivisors[prime] = 1

                n /= prime
                break #start from first prime.
            if i == len(primes)-1:
                addPrime(primes)

def numberOfDivisors(primeDivisors):
    result = 1
    for i in primeDivisors.values():
        result *= (i+1)

    return result

def addPrime(primes):
    i = primes[len(primes)-1]
    if(i==2):
        i = 1;

    while True:
        i += 2
        if(isPrime(i)):
            primes.append(i)
            return primes

def isPrime(n):
    if((n != 2) and (n%2==0)):
        return False; #even number

    i = 3;
    while(i*i < n):
        if n%i == 0:
            return False
        i += 2
    return True

def sumOfDivisors(n):
    sum = 0
    for i in range(1,n):
        if(n%i == 0):
            sum += i

    return sum

def isAmicable(a): #Pb21
    b = sumOfDivisors(a)
    if(a==b):
        return False
    if(a == sumOfDivisors(b)):
        return True
    else:
        return False

def readFileAndSplit(filename, splitor, refiner=lambda x: x):
    f = open(filename, 'r')
    data = [];
    for line in f:
        data.append([refiner(x) for x in line.rstrip().split(splitor)])
