def fibonnaci_seq_with_digits(n):
  fib = [1,1]
  found = False
  res = 0
  j = 0
  while(found == False):
    new = fib[j]+fib[j+1]
    if(len(str(new))==n):
      res = j+3
      found = True
    fib.append(new)
    j += 1
  return res
      
print(fibonnaci_seq_with_digits(1000))