nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
unions = [
    (4, 3),
    (3, 8),
    (6, 5),
    (9, 4),
    (2, 1),
    (8, 9),
    (5, 0),
    (7, 2),
    (6, 1),
    (1, 0),
    (6, 7)]


def is_connected(i, j):
    return root(j) == root(i)


def root(i):
    while i != nodes[i]:
        i = nodes[i]
    return i


def union(i, j):
    idx_i = root(i)
    nodes[idx_i] = root(j)


for to_unity in unions:
    union(to_unity[0], to_unity[1])

print(nodes)

for verify in unions:
    print(verify, is_connected(verify[0], verify[1]))
