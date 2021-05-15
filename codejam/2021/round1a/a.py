import sys
import copy
import operator
import math
import collections
import heapq
import itertools
import functools
import bisect

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solution(X):
    n = len(X)
    cnt = 0
    for i in range(1,n):
        a = X[i]
        b = X[i-1]
        """
        if a > b:
            continue
        else:
            while a <= b:
                for digit in range(0,10):
                    if a*10+digit > b:
                        a = a*10+digit
                        X[i] = a
                        cnt += 1
                        break
                else:
                    a = a*10
                    X[i] = a
                    cnt += 1
        """
        if a > b:
            continue
        else:
            if len(str(a)) == len(str(b)):
                a = a*10
                cnt += 1
            else:
                a = str(a)
                b = str(b)
                lendiff = len(b) - len(a)
                bfront = b[:-lendiff]
                if int(bfront) > int(a):
                    a += "0"*(lendiff+1)
                    cnt += (lendiff+1)
                elif int(bfront) == int(a):
                    # if bback not all 9 then possible
                    bback = b[-lendiff:]
                    #cand = str(int(bback)+1)
                    cand = str(int(bback) + 1).zfill(len(bback))
                    #eprint(a,b,bback,cand)
                    if len(cand) == len(bback):
                        a += cand
                        cnt += lendiff
                    else:
                        a += "0"*(lendiff+1)
                        cnt += (lendiff+1)
                else:
                    a += "0"*lendiff
                    cnt += lendiff
            a = int(a)
            X[i] = a
    eprint(X)
    return cnt

T = int(input()) # read num test cases
for case_num in range(1, T + 1):
    N = int(input())
    X = list(map(int,input().split()))
    res = solution(X)
    print("Case #{}: {}".format(case_num, res))
