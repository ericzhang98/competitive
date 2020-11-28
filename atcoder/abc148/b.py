n = int(raw_input())
s = raw_input().split()

res = []
for i in range(n):
    res.append(s[0][i])
    res.append(s[1][i])
print "".join(res)
