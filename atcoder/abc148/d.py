N = int(raw_input())
a = map(int, raw_input().split())

curr = 1
for ai in a:
    if ai == curr:
        curr += 1

if curr == 1:
    print -1
else:
    print len(a) - curr + 1
