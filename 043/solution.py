from itertools import permutations

def pandigital(n):
  n_list = list(str(n))

  return len(n_list)==10 and set(n_list)==set("0123456789")

def sum_pandigital():
  numbers = []
  divisors = [2,3,5,7,11,13,17]
  for p in permutations('0123456789'):
    if(p[0]=='0'):
      continue
    p_list = list(p)
    valid = True

    for j in range(7):
      num = int(p_list[j+1] + p_list[j+2] + p_list[j+3])
      if num % divisors[j] != 0:
        valid = False
        break

    if valid:
      numbers.append(int(''.join(p)))
  return sum(numbers)

print(sum_pandigital())