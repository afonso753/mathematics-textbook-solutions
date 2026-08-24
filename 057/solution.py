def continuos_fract(n):
  a = ['Null']
  b = [1]
  A = [1, 1]
  B = [0, 1]
  w = []
  for i in range(1,n+1):
    b.append(2)
    a.append(1)
    value_A = b[i]*A[i] + A[i-1]
    value_B = b[i]*B[i] + B[i-1]
    A.append(value_A)
    B.append(value_B)
    w.append(str(A[i+1])+'/'+str(B[i+1]))
  return w

def numerator_more_digits_denominator(n):
  n_list = list(n)
  num = []
  den = []
  found = False
  i = 0
  while (found == False):
    if(n_list[i] != '/'):
      num.append(n_list[i])
      i+=1
    else:
      den = n_list[(i+1):]
      found = True
  if (len(num)>len(den)):
    return True
  else:
    return False

def function():
  w = []
  fractions = continuos_fract(1000)
  for i in range(len(fractions)):
    if(numerator_more_digits_denominator(fractions[i])):
      w.append(fractions[i])
  return len(w)

print(function())

#I realize
