def multiples_3_5(n):
  w = []
  for i in range(3,n):
    if (i%3 == 0 or i%5 == 0):
      w.append(i)
  return sum(w)

print(multiples_3_5(10))
print(multiples_3_5(1000))
  