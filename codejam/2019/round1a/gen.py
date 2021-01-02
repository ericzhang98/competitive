with open('test_a_all', 'w') as f:
    f.write("1521\n")
    for i in range(2,41):
        for j in range(2,41):
            f.write(f"{i} {j}\n")
