from datetime import datetime as dt
# print(dt.now())#2022-12-27 14:34:24.041271
# print(dt.now().strftime("%B"))
# print(dt.now().strftime("%d"))#A reference of all the legal format code
# #strptime:used to convert the string format into date format
# print(dt.strptime("28 december, 2022","%d %B, %Y"))

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime as dt

# Complete the time_delta function below.
def time_delta(t1, t2):
    first=dt.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    second=dt.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    return str(abs(int((first-second).total_seconds())))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()