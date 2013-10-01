import sys

def fread(fname):
  f=open(fname,'r')
  a=(f.read()).split()
  print a
  return a

def freq(a):
  fr={}
  for i in a:
    fr[i]=fr.get(i,0)+1
  for  k,v in fr.items():
    print k,':',v 
  dec=sorted(fr.items(),key=lambda x:x[1],reverse=True)
  print dec

freq(fread(sys.argv[0]))
