def isPalindrome(n):
  n_list = list(map(int,list(str(n))))
  if (n_list == n_list[::-1]):
    return True
  else:
    return False

def largestPalindrome(lb, ub):
  largest = 0
  for i in range (lb, ub):
    for j in range (lb, ub):
      num = i*j
      if (isPalindrome(num) and num > largest):
        largest = num
  return largest

print(largestPalindrome(100, 999))