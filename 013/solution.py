with open('number.txt', 'r') as file:
  numbers = [int(line.strip()) for line in file]

sum = sum(numbers)
first_10 = str(sum)[:10]

print(first_10)