import random
random.seed(98)

with open('test_d', 'w+') as f:
    n = 1000
    f.write("%d\n" % n)

    for i in range(n):
        k_i = random.randint(1, 10)
        f.write("%d " % k_i)
        sample = random.sample(list(range(1,21)), k_i)
        for i, v in enumerate(sample):
            f.write("%d" % v)
            f.write(" \n"[i == len(sample)-1])
