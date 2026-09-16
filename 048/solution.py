def function(n):
  sum = 0
  for i in range(1, n+1):
    sum += i**i
  sum_list = list(map(int,list(str(sum))))
  sum_list_update = sum_list[-10:]
  print(sum_list_update)
  res = str(sum_list_update[0])
  for i in range(1,len(sum_list_update)):
    res +=str(sum_list_update[i])
  return res


print(function(1000))