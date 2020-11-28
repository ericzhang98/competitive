t = int(raw_input())

def soln(a, s):
    """
    m = -1
    mi = -1
    tot = 0
    for i, v in enumerate(a):
        tot += v
        temp = mi
        if v > m:
            m = v
            temp = i
        if tot - m > s:
            return mi + 1
        mi = temp
    return 0 if tot <= s else mi+1
    """
    m = -1
    mi = -1
    ni = -1
    tot = 0
    ans = 0
    for i, v in enumerate(a):
        tot += a[i]
        if v > m:
            m = v
            mi = i+1
        if tot <= s and i+1 > ni:
            ans = 0
            ni = i+1
        if tot - m <= s and i > ni:
            ans = mi
            ni = i

    return ans

for _ in range(t):
    n, s = map(int, raw_input().split())
    a = map(int, raw_input().split())
    print soln(a, s)
