#the problem is equivalent to find the unique pair(a,b) s.t. a+b-ab/1000=500

import math

def pyth():
  for a in range (1, 1000):
    for b in range (1, 1000):
      if(a+b-1/1000*a*b == 500):
        return [a,b]

list = pyth()
list.append(1000-list[0]-list[1])         #c is equal to 1000-a-b
res = math.prod(list)

print(res)
