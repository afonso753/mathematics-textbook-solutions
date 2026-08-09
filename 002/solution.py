def fibonacci(n):
  if (n==1):
    return [1]
  elif (n==2):
    return [1,2]
  else:
    w = [1,2]
    for i in range(n-2):
      f = w[i]+w[i+1]
      w.append(f)
  return w

def first_fibonnaci_geq(n):
  res = 0
  j = 0
  while (res < n):
    res = fibonacci(j)[-1]
    j+=1
  return j

def even_fibbonaci(n):
  w = []
  for i in range(len(fibonacci(n))):
    fib = fibonacci(n)[i]
    if (fib%2 == 0):
      w.append(fib)
  return w

ub = first_fibonnaci_geq(4*10**6)

print(sum(even_fibbonaci(ub-1)))