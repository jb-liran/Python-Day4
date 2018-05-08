import  fileinput
import sys,glob

s1 = raw_input("enter name:")


print "hello",s1, sys.argv

if sys.platform == "win32":
   sys.argv[1:] = glob.glob(sys.argv[1])

print sys.argv

for line in fileinput.input():
      print (fileinput.filename())
      print (line + ':' + str(fileinput.lineno()))

	  
	  
	  