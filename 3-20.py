import sys
import re

def grep(fname,word):
  f=open(fname,'r')
  a=f.readlines()
  #print a,word
  for i in a:
    w=re.search(word,i)
    if w:
       print i 
  f.close()

def main():
  grep(sys.argv[0],'def')

if __name__=='__main__':
  main()


