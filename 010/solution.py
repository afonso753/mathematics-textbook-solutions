import math

def isPrime(n):
    if (n < 2):
        return False
    for i in range (2, int(math.sqrt(n))+1):
        if (n%i == 0):
            return False
    return True

def sumPrimesBellow(k):
    primes = [2]
    for i in range(1, k, 2):
        if (isPrime(i)):
            primes.append(i)
    return sum(primes)

print(sumPrimesBellow(2*10**6))