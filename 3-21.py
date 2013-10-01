import re,sys

def wrap(fname,no):
  f=open(fname,'r')
  a=f.readlines()
  print a,no
  for i in a:
    #print i
    if(len(i)>no):
      print i[0:no]
      print i[no:]   
    else:
      print i
def main():
  wrap(sys.argv[0],30)
 
if __name__=='__main__':
  main()

''''sdsafdnfdm,n,dnsf,mndsmnfdsnmfnmdsmnfndsmfndsmndmnd'''
