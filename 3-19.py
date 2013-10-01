import sys

def head(fname,i=0):
  f=open(fname,'r')
  while(i<10):
    a=f.readline()
    print a
    i=i+1

def tail(fname):
  f=open(fname,'r')
  a=f.readlines()
  b=[i for i in a[::-1]]
  print b
  

def main():
  head(sys.argv[0])
  print 'Tailing operation\n'
  tail(sys.argv[0])
  

if __name__=='__main__':
  main()
