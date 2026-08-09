def evenly_divisible(n):
  i = 2520
  j = 1
  while (j <= n):
    if(i%j == 0):
      j+=1
    else:
      j = 1
      i += 1
  return i

print(evenly_divisible(20))
    