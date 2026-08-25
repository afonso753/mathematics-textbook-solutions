def function(n):
  p_value = 0
  lenn = 0
  for p in range(1,n+1):
    w = []
    lim = int(p/2)+1
    for a in range(1,lim):
      for b in range(1,lim):
        if (p**2-2*p*(a+b)+2*a*b == 0):
          c = p - a - b
          w.append({a,b,c})
    if(len(w)>lenn):
      lenn = len(w)
      p_value = p
  return p_value


print(function(1000))