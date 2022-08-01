from sys import argv
from os.path import exists
#from_file can also be called argv[1]
script, from_file, to_file = argv
open(argv[2], 'w').write(open(argv[1]).read())
