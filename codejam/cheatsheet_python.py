def mat_to_str(mat):
    l = []
    for row in mat:
        l.append(" ".join(map(str,row)))
    return "\n".join(l)

