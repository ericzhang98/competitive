# raw_input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input()) # read a line with a single integer
for test_case in xrange(1, t + 1):
    area = int(raw_input())

    import sys

    if area == 20:
        # make rectangle that's 4x5, top left corner (100, 100)
        rect = [[0]*5 for i in range(4)]
        for i in range(250):
            print "101 101"
            sys.stdout.flush()
            x, y  = raw_input().split(" ")
        for i in range(250):
            print "103 101"
            sys.stdout.flush()
            x, y  = raw_input().split(" ")
        for i in range(250):
            print "102 102"
            sys.stdout.flush()
            x, y  = raw_input().split(" ")
        for i in range(250):
            print "103 102"
            sys.stdout.flush()
            x, y  = raw_input().split(" ")
            if x == 0:
                break
