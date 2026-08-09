import math

def isPrime(n):
    if (n < 2):
        return False
    for i in range (2, int(math.sqrt(n))+1):
        if (n%i == 0):
            return False
    return True
            

def largestPrime(n):
    i=2
    r=1
    while(i<=n):
        if(n%i==0 and isPrime(i)):
            r=i
        i+=1
    return r


print(largestPrime(600851475143))