import math

def triangleNumber(k):
    tri = (k*(k+1))/(2)
    return int(tri)

def first_triang_with_divisors(k):
    i = 1
    while (True):
        divisors = 0
        triang = triangleNumber(i)
        ub = int(math.sqrt(triang))+1
        for j in range(1, ub):
            if(triang%j == 0):
                if(triang/j == j):
                    divisors += 1
                else:
                    divisors += 2
        if(divisors > k):
            return triang
        i += 1

print(first_triang_with_divisors(500))