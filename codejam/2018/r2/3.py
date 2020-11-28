# raw_input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input()) # read a line with a single integer
for asdf in xrange(1, t + 1):

    M = raw_input()
    M = int(M)

    formulas = []
    for m in range(M):
        c = raw_input().split(" ")
        nums = []
        for x in c:
            nums.append(int(x))
        formulas.append(nums)

    g = raw_input().split(" ")
    grams = []
    for gg in g:
        grams.append(int(gg))



    def solution(M, formulas, grams):
        # can't make lead without using lead
        if formulas[0][0] == 1 or formulas[0][1] == 1:
            return grams[0]

        two_i = formulas[0]
        if grams[two_i[0]-1] > grams[two_i[1]-1]:
            grams[0] += grams[two_i[1]-1]
            grams[two_i[1]-1] = 0
            grams[two_i[0]-1] -= grams[two_i[1]-1]
        elif grams[two_i[1]-1] > grams[two_i[0]-1]:
            grams[0] += grams[two_i[0]-1]
            grams[two_i[0]-1] = 0
            grams[two_i[1]-1] -= grams[two_i[0]-1]
        else:
            grams[0] += grams[two_i[0]-1]
            grams[two_i[0]-1] = 0
            grams[two_i[1]-1] -= grams[two_i[0]-1]





    res = solution(M, formulas, grams)

    print "Case #{}: {}".format(asdf, res)

