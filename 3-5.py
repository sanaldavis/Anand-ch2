def pro(a,s=1):
  for i in a:
    s=s*i
  print s
def fact(b):
  a=range(b)
  a.append(b)
  pro(a[1:])
fact(5)

