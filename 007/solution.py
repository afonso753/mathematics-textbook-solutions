import math

def isPrime(n):
  if (n<2):
    return False
  elif(n%2==0 and n!=2):
    return False
  else:
    for i in range (2,int(math.sqrt(n))+1):
      if(n%i == 0):
        return False
  return True

def primeMaker(k):
  i = 2
  primes = []
  while (len(primes) < k):
    if(isPrime(i)):
      primes.append(i)
    i+=1
  return primes[-1]

print(primeMaker(10001))