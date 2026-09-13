def function():
  nums = []
  for i in range(10,100):
    value_list = list(map(int,list(str(i))))
    if(value_list[0]**5+value_list[1]**5 == i):
      nums.append(i)
  for i in range(100,1000):
      value_list = list(map(int,list(str(i))))
      if(value_list[0]**5+value_list[1]**5+value_list[2]**5 == i):
        nums.append(i)
  for i in range(1000,10000):
      value_list = list(map(int,list(str(i))))
      if(value_list[0]**5+value_list[1]**5+value_list[2]**5+value_list[3]**5 == i):
        nums.append(i)
  for i in range(10000,100000):
      value_list = list(map(int,list(str(i))))
      if(value_list[0]**5+value_list[1]**5+value_list[2]**5+value_list[3]**5+value_list[4]**5 == i):
        nums.append(i)
  for i in range(100000,1000000):
      value_list = list(map(int,list(str(i))))
      if(value_list[0]**5+value_list[1]**5+value_list[2]**5+value_list[3]**5+value_list[4]**5+value_list[5]**5 == i):
        nums.append(i)



  return sum(nums)


print(function())