import base64
import sys

fname = sys.argv[1]

with open(fname, 'rb') as o:
	buff = o.read()

with open(fname+'.85rec', 'wb') as o:
	o.write(base64.b85decode(buff))