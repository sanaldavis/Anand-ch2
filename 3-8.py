def cus(a):
  b=[]
  for i in a:
   if not b: 
     b.append(i)
   else:  
     b.append(i+b[-1])
  print b
cus([1,2,3,4])
cus([4,3,2,1])
