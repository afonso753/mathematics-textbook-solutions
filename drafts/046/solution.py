import math

def isPrime(n):
  if(n<2):
    return False
  if(n>2 and n%2==0):
    return False
  for i in range(3,int(math.sqrt(n))+1,2):
    if(n%i==0):
      return False
  return True

def function():
  found = False
  i = 3
  while(found == False):
    if (isPrime(i)):
      i+=2
    for j in range():
      for k in range()