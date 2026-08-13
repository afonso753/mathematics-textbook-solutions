def sum_diagonals():
  sum = 1
  last = 1
  for i in range(1, 501):
    sum_1 = last + 2*i  
    sum_2 = sum_1 + 2*i
    sum_3 = sum_2 + 2*i
    sum_4 = sum_3 + 2*i
    sum += sum_1 + sum_2 + sum_3 + sum_4
    last = sum_4
  return (sum)

print(sum_diagonals()) 