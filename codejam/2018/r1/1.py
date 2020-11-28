# raw_input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input()) # read a line with a single integer
for asdf in xrange(1, t + 1):
    r, c, h, v = raw_input().split(" ")
    r, c, h, v = int(r), int(c), int(h), int(v)
    
    waffle = []
    num_chips = 0
    for row in range(r):
        chars = list(raw_input())
        for ch in chars:
            if ch == '@':
                num_chips += 1
        waffle.append(chars)


    # greedy strategy -- doesn't matter whether u do horizontal/vertical first
    # each vetical/horizontal cut must eventually lead to an equal assignment along that axis
    # thus keep going as we iterate thru until we reach num/cut_num


    if num_chips == 0:
        res = "POSSIBLE"
        print "Case #{}: {}".format(asdf, res)
        continue

    if num_chips % ((h+1)*(v+1)) != 0:
        res = "IMPOSSIBLE"
        print "Case #{}: {}".format(asdf, res)
        continue

    # let's just do horizontal cuts first
    target_num = num_chips/(h+1) # each slice must aim to get exactly this much
    h_slices = []
    curr_slice_start = 0
    curr_num = 0
    should_go = True
    for i in range(r):
        if curr_num == target_num:
            h_slices.append(waffle[curr_slice_start:i])
            curr_slice_start = i
            curr_num = 0 

        if curr_num < target_num:
            for ch in waffle[i]:
                if ch == '@':
                    curr_num += 1
        else:
            should_go = False
            break

    if curr_num == target_num or curr_num == 0:
        if curr_num != 0:
            h_slices.append(waffle[curr_slice_start:])
            curr_num = 0 
            for ch in waffle[i]:
                if ch == '@':
                    curr_num += 1
    else:
        should_go = False

    if should_go:
        #print h_slices
        should_go = True
        target_num = num_chips/((h+1)*(v+1))
        curr_num = 0
        each_slice_num = [0]*len(h_slices) # keep track of each slice's count
        for j in range(c): #iterate thru possible slicings
            #print curr_num
            if curr_num == target_num:
                for s in range(len(h_slices)-1):
                    if each_slice_num[s] != each_slice_num[s+1]:
                        should_go = False
                curr_num = 0
                for n in range(len(each_slice_num)):
                    each_slice_num[n] = 0

            if curr_num < target_num:
                for s in range(len(h_slices)):
                    for hs in h_slices[s]:
                        if hs[j] == '@':
                            each_slice_num[s] += 1
                curr_num = min(each_slice_num)
                #print each_slice_num

            else:
                should_go = False

            if not should_go:
                break

        # last h check
        #print should_go
        if should_go:
            if curr_num == target_num or curr_num == 0:
                for s in range(len(h_slices)-1):
                    if each_slice_num[s] != each_slice_num[s+1]:
                        should_go = False
            else:
                should_go = False

    if should_go:
        res = "POSSIBLE"
        print "Case #{}: {}".format(asdf, res)
    else:
        res = "IMPOSSIBLE"
        print "Case #{}: {}".format(asdf, res)
