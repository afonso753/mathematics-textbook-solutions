with open('grid.txt', 'r') as file:
  grid = [
    [int(x) for x in line.split()]
    for line in file
  ]

def largest_product_horizontal():
  largest = 0
  for i in range(len(grid)):
    for j in range(17):
      prod = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
      if (largest < prod):
        largest = prod
  return largest

def largest_product_vertical():
  largest = 0
  for i in range(len(grid[1])):
    for j in range(17):
      prod = grid[j][i]*grid[j+1][i]*grid[j+2][i]*grid[j+3][i]
      if (largest < prod):
        largest = prod
  return largest

def largest_product_diagonal_right():
  largest = 0
  for i in range(17):
    for j in range(17):
      prod = grid[j][i]*grid[j+1][i+1]*grid[j+2][i+2]*grid[j+3][i+3]
      if(largest < prod):
        largest = prod
  return largest

def largest_product_diagonal_left():
  largest = 0
  for i in range(17):
    for j in range(1,18):
      prod = grid[i][-j]*grid[i+1][-j-1]*grid[i+2][-j-2]*grid[i+3][-j-3]
      if(largest < prod):
        largest = prod
  return largest

print(grid)

print(max(
  largest_product_horizontal(),
  largest_product_vertical(),
  largest_product_diagonal_left(),
  largest_product_diagonal_right()
  ))