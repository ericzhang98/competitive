# raw_input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input()) # read a line with a single integer
for asdf in xrange(1, t + 1):
    c = raw_input()
    arr = map(int, raw_input().split())



    def solution(c, arr):
        if sum(arr) != c:
            return "IMPOSSIBLE"
        if arr[0] == 0 or arr[-1] == 0:
            return "IMPOSSIBLE"

        arr[0] -= 1
        arr[1] -= 1

        if c == 2:
            return "1\n.."
        if c == 3:
            return "

            


    res = solution(c, arr)

    print "Case #{}: {}".format(asdf, res)
