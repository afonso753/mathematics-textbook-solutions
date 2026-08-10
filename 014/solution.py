def collatz_sequence(n):
  w=[n]
  k=n
  while(k!=1):
    if(k%2==0):
      k=int(k/2)
      w.append(k)
    else:
      k=3*k+1
      w.append(k)
  return w

def longest_collatz_chain_under(n):      #set is a more efficient way to create the data repeated istead of, say list.
  chain = 10
  number = 13
  repeated = set()
  for i in range(1, n):
    if(i not in repeated):
      c = collatz_sequence(i)
      repeated.update(c)
      if (len(c) > chain):
        chain = len(c)
        number = i
  return number

print(longest_collatz_chain_under(10**6))