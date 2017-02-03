import sys
import os

cwd = os.getcwd()   #current Working Directory

sys.path.append(cwd)
#print(sys.path)

#Test the module: generate_list
from generate_list import printIt
for i in range(1000):
    print"round: %d" % (i+1)
    printIt()