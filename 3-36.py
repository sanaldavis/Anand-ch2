import itertools

def ana(a):
  b=[]
  for i in a: 
    for j in a:
      print i
      k=tuple(i)
      c=itertools.permutations(j)
      if k in c:
        b.append(j)
   len(b) 
   break
  print b

ana(['sanal','ate','eat','tea'])  
