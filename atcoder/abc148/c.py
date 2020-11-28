A, B = map(int, raw_input().split())

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

print A * B / gcd(A, B)
