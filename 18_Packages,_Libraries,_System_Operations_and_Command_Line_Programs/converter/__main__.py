import sys
from converter import *

if sys.argv[1] == "-ctof":
    print(cel_to_feh(float(sys.argv[2])))

elif sys.argv[1] == "-ftoc":
    print(feh_to_cel(float(sys.argv[2])))
