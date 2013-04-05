import sys
import os
fname = sys.argv[1]
address = sys.argv[2]
owd = os.getcwd()
f = open(fname,"rb")
data = f.read()
os.chdir(address)
o = open(fname,"a+b")
o.write(data)
'''for line in f:
	os.chdir(address)
	o = open(fname,"a+b")
	o.write(line)
	o.close()
	os.chdir(owd)
f.close()'''