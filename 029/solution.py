def function():
  data = set()
  for a in range(2, 101):
    for b in range(2, 101):
      value = a**b
      data.add(value)
  return len(data)

#sets don't admit duplicates

print(function())