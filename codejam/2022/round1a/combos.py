import itertools
import collections

"""
cands = {}
asdf = {1,2,4,8,9}
for i in range(len(asdf)+1):
    for tup in itertools.combinations(list(asdf), i):
        left = set(list(tup))
        right = asdf - left
        diff = sum(left) - sum(right)
        if diff in {0,1,2,3,4,5,6,7,8,9}:
            cands[diff] = left
print(cands)
"""

final_list = [1, 4, 6, 9, 11, 14, 16, 19, 21, 49, 51, 99, 101, 149, 151, 199, 201, 499, 501, 999, 1001, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127, 1128, 1129, 1130, 1131, 1132, 1133, 1499, 1501, 1999, 2001, 4999, 5001, 9999, 10001, 14999, 15001, 19999, 20001, 37961, 49999, 50001, 99999, 100001, 149999, 150001, 199999, 200001, 499999, 500001, 999999, 1000001, 1499999, 1500001, 1999999, 2000001, 4999999, 5000001, 9999999, 10000001, 14999999, 15000001, 19999999, 20000001, 49999999, 50000001, 99999999, 100000001, 149999999, 150000001, 199999999, 200000001]
def make_left_right(test):

    places = {}
    for place in range(1,10):
        one = [10**place//2+1,10**place//2-1]
        two = [10**place+1,10**place-1]
        three = [10**place*3//2+1,10**place*3//2-1]
        four = [10**place*2+1,10**place*2-1]
        places[place] = [one,two,three,four]
        #print(one, two, three, four)

    test = str(test)
    digits = [0]*9
    for i in range(len(test)):
        digits[-1-i] = int(test[-1-i])
    last_digit = digits[-1]
    digits.pop(-1)

    #print(digits)

    left = set()
    right = set()
    two_count = 0

    for i in range(8):
        place = 8-i
        digit = digits[i]
        #print(place, digits[i])
        one,two,three,four = places[place]
        everything = set(one+two+three+four)
        l = {one[0],two[1],three[0],four[1]}
        if digit == 0:
            pass
        elif digit == 1:
            l.add(one[1])
            if two_count == 0:
                l.remove(two[1])
                l.add(two[0])
                two_count += 1
            else:
                two_count -= 1
        elif digit == 2:
            l.add(two[0])
            if two_count == 1:
                l.remove(one[0])
                l.add(one[1])
                two_count -= 1
            else:
                two_count += 1
        elif digit == 3:
            l.add(three[1])
            if two_count == 0:
                l.remove(two[1])
                l.add(two[0])
                two_count += 1
            else:
                two_count -= 1
        elif digit == 4:
            l.add(four[0])
            if two_count == 1:
                l.remove(one[0])
                l.add(one[1])
                two_count -= 1
            else:
                two_count += 1
        elif digit == 5:
            l.add(two[0])
            l.add(three[1])
        elif digit == 6:
            l.add(two[0])
            l.add(four[0])
            l.remove(one[0])
            l.add(one[1])
        elif digit == 7:
            l.add(three[1])
            l.add(four[0])
        elif digit == 8:
            l.add(one[1])
            l.add(three[1])
            l.add(four[0])
            if two_count == 0:
                l.remove(two[1])
                l.add(two[0])
                two_count += 1
            else:
                two_count -= 1
        elif digit == 9:
            l.add(two[0])
            l.add(three[1])
            l.add(four[0])
            if two_count == 1:
                l.remove(one[0])
                l.add(one[1])
                two_count -= 1
            else:
                two_count += 1
        assert two_count == 0 or two_count == 1
        r = everything - l
        left = left.union(l)
        right = right.union(r)

    remainder = last_digit
    if two_count == 1:
        remainder -= 2

    #print(sum(left) - sum(right), two_count, last_digit, remainder)

    assert remainder in {-1,1,3,5,7,9}
    while remainder not in {-1,1}:
        remainder -= 4
        for x in left:
            if x + 2 in right:
                left.remove(x)
                left.add(x+2)
                right.remove(x+2)
                right.add(x)
                break

    assert remainder in {-1,1}
    if remainder == 1:
        left.add(1)
    else:
        right.add(1)

    #1100..1133
    filler_left = set(range(1100,1134))
    #37961
    filler_right = {37961}

    left |= filler_left
    right |= filler_right

    assert sum(left) - sum(right) == int(test)
    assert len(left) + len(right) == 100

    return left, right

make_left_right(3)
make_left_right(123456797)
