import html
import sys
from html.entities import html5

if(len(sys.argv) == 1):
	  raise Exception("ERROR: No argument supplied")
if(len(sys.argv) > 2):
	  raise Exception("ERROR: Too many arguments")

encoded_string = ''.join(['&#{};'.format(ord(c)) if ord(c) not in html5 else c for c in str(sys.argv[1])])

print(encoded_string) 
