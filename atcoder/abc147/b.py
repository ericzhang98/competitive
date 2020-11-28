# -*- coding: utf-8 -*-
# get a string
s = raw_input()

if len(s) % 2 == 0:
    i, j = len(s)/2-1, len(s)/2
else:
    i, j = len(s)/2-1, len(s)/2 + 1

ans = 0
while i >= 0:
    if s[i] != s[j]:
        ans += 1
    i -= 1
    j += 1

print ans
