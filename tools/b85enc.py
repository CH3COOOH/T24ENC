import base64
import sys

fname = sys.argv[1]

with open(fname, 'rb') as o:
	buff = o.read()

with open(fname+'_b85.txt', 'w') as o:
	o.write(base64.b85encode(buff).decode('utf-8'))