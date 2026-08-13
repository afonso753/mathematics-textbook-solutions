import math

def isPrime(n):
  if(n<2):
    return False
  if(n%2==0 and n>2):
    return False
  for j in range(3, int(math.sqrt(n))+1,2):
    if(n%j==0):
      return False
  return True

def product_coef():
  count = 0
  a = 0
  b = 0
  for i in range(-999, 1000):
    for j in range(-1000, 1001):
      n = 0
      count_v = 0
      found = True
      while (found == True):
        value = n*n+i*n+j 
        if(isPrime(value)):
          count_v += 1
          n += 1
        else:
          if(count_v > count):
            count = count_v
            a = i
            b = j
          found = False
  return a*b
        
print(product_coef())