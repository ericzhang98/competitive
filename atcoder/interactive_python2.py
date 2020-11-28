import sys
import time

def mergesort(letters):
    if len(letters) == 1: return letters
    l1 = mergesort(letters[:len(letters)//2])
    l2 = mergesort(letters[len(letters)//2:])
    return merge(l1, l2)

def merge(l1, l2):
    i1, i2 = 0, 0
    result = []
    while i1 < len(l1) and i2 < len(l2):
        if lt(l1[i1], l2[i2]):
            result.append(l1[i1])
            i1 += 1
        else:
            result.append(l2[i2])
            i2 += 1
    result = result + l1[i1:] + l2[i2:]
    return result

def lt(c1, c2):
    print("? {} {}".format(c1, c2))
    sys.stdout.flush()
    response = raw_input()
    if response == '<':
        return True
    else:
        return False

N, Q = map(int, raw_input().split())

if N == 26:
    letters = [chr(ord('A') + i) for i in range(N)]
    letters = mergesort(letters)
    print("! {}".format(''.join(letters)))
    sys.stdout.flush()

elif N == 5:
    l = [chr(ord('A') + i) for i in range(N)]
    a,b,c,d,e = l
    
    if lt(b, a):
        a, b = b, a

    if lt(d, c):
        c, d = d, c

    if lt(c, a):
        c, d, a, b = a, b, c, d

    if lt(e, c):
        if lt(c, b):
            if lt(d, b):
                if lt(e, a):
                    print("! {}{}{}{}{}".format(e, a, c, d, b))
                else:
                    print("! {}{}{}{}{}".format(a, e, c, d, b))
            else:
                if lt(e, a):
                    print("! {}{}{}{}{}".format(e, a, c, b, d))
                else:
                    print("! {}{}{}{}{}".format(a, e, c, b, d))

        else:
            if lt(b, e):
                print("! {}{}{}{}{}".format(a, b, e, c, d))
            else:
                if lt(a, e):
                    print("! {}{}{}{}{}".format(a, e, b, c, d))
                else:
                    print("! {}{}{}{}{}".format(e, a, b, c, d))
    else:
        if lt(d, e):
            if lt(b, d):
                if lt(b, c):
                    print("! {}{}{}{}{}".format(a, b, c, d, e))
                else:
                    print("! {}{}{}{}{}".format(a, c, b, d, e))
            else:
                if lt(b, e):
                    print("! {}{}{}{}{}".format(a, c, d, b, e))
                else:
                    print("! {}{}{}{}{}".format(a, c, d, e, b))
        else:
            if lt(b, e):
                if lt(b, c):
                    print("! {}{}{}{}{}".format(a, b, c, e, d))
                else:
                    print("! {}{}{}{}{}".format(a, c, b, e, d))
            else:
                if lt(b, d):
                    print("! {}{}{}{}{}".format(a, c, e, b, d))
                else:
                    print("! {}{}{}{}{}".format(a, c, e, d, b)) 

