import random
seed = random.randint(1,1000)
print seed
random.seed(seed)
arr = []
for i in range(100000):
    arr.append(random.randint(1, 100000))

open('test_e', 'w').close()
with open('test_e', 'w') as f:
    f.write("100000 50000\n")
    for x in arr:
        f.write(str(x) + " ")
