# raw_input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input()) # read a line with a single integer
for asdf in xrange(1, t + 1):
    n, l = raw_input().split(" ")
    n, l = int(n), int(l)

    c = raw_input().split(" ")
    nums = []

    for x in c:
        nums.append(int(x))

    def solution(n, l, nums):
        remaining = n
        for num in nums:
            remaining = remaining - num

        from collections import defaultdict
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        counts[0] = remaining

        hm = {}
        for x in range(n):
            hm[x] = (x*1000/n) % 10

        # print hm

        count = 0
        for x in hm:
            if hm[x] >= 5:
                # print "%d works, count: %d" % (x, count)
                for i in range(x-count, x+1):
                    hm[i] = x-i
                count = 0
            else:
                count += 1

        """
        if count > 0:
            print "0!"
            for i in range(len(hm)-count, len(hm)):
                hm[i] = len(hm)-i
        """

        if count == len(hm):
            # print "Doesn't matter"
            return 100
        elif count > 0:
            for i in range(len(hm)-count, len(hm)):
                hm[i] = len(hm)-i

        order = sorted(range(n), key=hm.get)
        # print hm
        #print order

        for o in order:
            if hm[o] == 0:
                counts[o] = counts[o]
            else:
                for x in range(counts[o]):
                    """
                    remaining -= hm[o]
                    if remaining < 0:
                        break
                    """
                    if remaining - hm[o] < 0:
                        counts[1] += remaining
                        remaining = 0
                        break
                    else:
                        remaining -= hm[o]
                    counts[o] -= 1
                    counts[o+hm[o]] += 1

            if remaining <= 0:
                break

        #print counts
        res = 0
        for key in counts:
            for x in range(counts[key]):
                res += round(float(100*key)/n)
        return int(res)

    res = solution(n, l, nums)

    print "Case #{}: {}".format(asdf, res)
