def dup(a):
  b,c=[],[]
  for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
  print c
dup([1,2,1,3,2,5])

