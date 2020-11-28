import sys
import itertools
import copy
import heapq
import bisect
from collections import defaultdict, Counter, deque
import re


params = ""
for line in sys.stdin:
    params += line

params = params.split("\n")

arr = [[c for c in l] for l in params]


d = {
       '**** ** ** ****' : '0',
       '  *  *  *  *  *' : '1',
       '***  *****  ***' : '2',
       '***  ****  ****' : '3',
       '* ** ****  *  *' : '4',
       '****  ***  ****' : '5',
       '****  **** ****' : '6',
       '***  *  *  *  *' : '7',
       '**** ***** ****' : '8',
       '**** ****  ****' : '9',
    }

good = True
nums = ""
for j in range(0, len(arr[0]), 4):
    text = "".join(reduce(lambda a, b: a+b, [arr[i][j:j+3] for i in range(len(arr))]))
    if text not in d:
        good = False
        break

    nums += d[text]

if good and int(nums) % 6 == 0:
    print "BEER!!"
else:
    print "BOOM!!"
