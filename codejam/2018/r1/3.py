# raw_input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input()) # read a line with a single integer
for asdf in xrange(1, t + 1):

    num, p = raw_input().split(" ")
    num, p = int(num), int(p)

    squares = []
    ranges = []
    start_p = 0
    import math
    for n in range(num):
        w, h = raw_input().split(" ")
        w, h = int(w), int(h)
        squares.append((w, h))
        ranges.append((2*min(w, h), 2*math.sqrt(w**2 + h**2)))
        start_p += (2*w + 2*h)

    prob3(num, p, start_p, w, h)


def prob3(num, p, start_p, w, h):

    goal_p = p - start_p
    curr_range = [0, 0]


    """
    for r in sorted(ranges):
        if curr_range[0] < goal_p:
            curr_range[0] += r[0]
            curr_range[1] += r[1]

    """
    for tup in ranges:
        curr_range[0] += tup[0]
        curr_range[1] += tup[1]

    # curr_range = [sum of mins, sum of maxes]

    if curr_range[1] <= goal_p:
        res = start_p + curr_range[1]
        print "Case #{}: {}".format(asdf, res)

    else:
        if curr_range[0] <= goal_p:
            res = p
            print "Case #{}: {}".format(asdf, res)

        else:
            res = p
            print "Case #{}: {}".format(asdf, res)
