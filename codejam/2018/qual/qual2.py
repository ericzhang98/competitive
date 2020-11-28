# raw_input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input()) # read a line with a single integer
for test_case in xrange(1, t + 1):
    num = raw_input()
    arr = [int(x) for x in raw_input().split(" ")] # read a list of integers, 2 in this case

    """
    def trouble_sort(l):
        done = False
        while not done:
            done = True
            for i in range(len(l)-2):
                if l[i] > l[i+2]:
                    done = False
                    temp = l[i+2]
                    l[i+2] = l[i]
                    l[i] = temp

    sorted_arr = sorted(arr)
    trouble_sort(arr)
    if sorted_arr == arr:
        print "Case #{}: {}".format(test_case, "OK")
    else:
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                print "Case #{}: {}".format(test_case, i)
                break
    """

    even_arr = arr[::2]
    odd_arr = arr[1::2]

    even_arr = sorted(even_arr)
    odd_arr = sorted(odd_arr)

    res_arr = [even_arr[i/2] if i%2 == 0 else odd_arr[i/2] for i in range(len(even_arr)+len(odd_arr))]

    sorted_res_arr = sorted(res_arr)
    
    if res_arr == sorted_res_arr:
        print "Case #{}: {}".format(test_case, "OK")
    else:
        for i in range(len(res_arr)-1):
            if res_arr[i] > res_arr[i+1]:
                print "Case #{}: {}".format(test_case, i)
                break
