# raw_input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    d, p = raw_input().split(" ") # read a list of integers, 2 in this case
    max_damage = int(d)
    attack_string = str(p)
    current_damage = 0
    beam_attack = 1
    num_attacks = 0
    from collections import defaultdict
    beam_nums = defaultdict(int)
    for c in attack_string:
        if c == 'C':
            beam_attack = beam_attack*2
        else:
            current_damage += beam_attack
            num_attacks += 1
            beam_nums[beam_attack] += 1
    
    if num_attacks > max_damage:
        res = "IMPOSSIBLE"
        print "Case #{}: {}".format(i, res)

    else:
        overdamage = current_damage - max_damage
        res = 0
        highest = beam_attack
        while overdamage > 0:
            # make highest the highest level beam after current swaps
            while beam_nums[highest] == 0:
                highest = highest/2
            beam_nums[highest] -= 1
            beam_nums[highest/2] += 1
            overdamage -= highest/2
            res += 1
        print "Case #{}: {}".format(i, res)
