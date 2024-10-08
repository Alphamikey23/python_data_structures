#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    result = []
    mylist = re.split(r'(\s+)', s)
    #res = [u for x in text.split('  ') for u in (x, '  ')]
    #print(mylist)

    if len(mylist) > 1:
        for x in mylist:
            result.append(x[0].capitalize() + x[1:])
    else:
        result.append(x.capitilize())
        
    #print(result)
    myresult = "".join(result)
    return myresult
    
    

if __name__ == '__main__':
    

    s = input()

    result = solve(s)

    print(result)


