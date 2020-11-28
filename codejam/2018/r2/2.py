# raw_input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input()) # read a line with a single integer
for asdf in xrange(1, t + 1):
    arr = map(int, raw_input().split())
    red = arr[0]
    blue = arr[1]


    def solution(red, blue):
        same = 2*min(red, blue)
        n = 0
        c = 1
        d = 0

        while same - 2*c >= 0:
            same -= 2*c
            c += 1
            n += 1

        diff = abs(red - blue)
        diff += same/2
        r = same/2

        while diff - c >= 0 and r > 0:
            diff -= c
            r -= 1


        
        """
        while same - c >= 0:
            same -= c
            d += 1
            if d == c+1:
                c += 1
                d = 0

            n += 1

        r = same/2
        diff = abs(red - blue)
        diff += r

        while diff - c >= 0 and r > 0:
            diff -= c
            r -= 1
            n += 1

        while diff - c >= 0:
            diff -= c
            c += 1
            n += 1
        """

        return n

        



    res = solution(red, blue)

    print "Case #{}: {}".format(asdf, res)

