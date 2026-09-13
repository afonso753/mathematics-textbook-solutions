def function(n):
  w = [n]
  for i in w:
    i_list = list(map(int,list(str(i))))
    num = 0
    for d in i_list:
      num += d*d
    if num == 1 or num == 44 or num == 32 or num == 13 or num == 10:
      return 0
    elif num == 89 or num == 89 or num == 145 or num == 42 or num == 20 or num == 4 or num == 16 or num == 37 or num == 58:
      return 1
    else:
      w.append(num)

def function2():
  count = 0
  for k in range(1,10*10**6):
    count = count + function(k)
  return count

print(function2())
