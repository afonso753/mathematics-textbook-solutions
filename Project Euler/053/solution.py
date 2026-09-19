def factorial(n):
  res = 1
  for i in range(2,n+1):
    res*=i
  return res

def combinatorics(n,r):
  res = factorial(n)/(factorial(r)*factorial(n-r))
  return int(res)

def function():
  count = 0
  for n in range(1,101):
    if(n%2!=0):
      for r in range(int(n/2)+1):
        if(combinatorics(n,r)>10**6):
          count+=2
    if(n%2==0):
      for r in range(int(n/2)+1):
        if(combinatorics(n,r)>10**6):
          if(r!=n/2):
            count+=2
          else:
            count+=1
  return count


print(function())