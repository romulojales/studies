#https://www.hackerrank.com/challenges/dynamic-array

n_seqs, queries = map(int, input().strip().split())
seqList = []
lastAns = 0

for _ in range(n_seqs):
    seqList.append([])

for i in range(n_seqs):
    query_type, x, y = map(int, input().strip().split())
    index = (x ^ lastAns) % n_seqs
    if query_type == 1:
        seqList[index].append(y)
    else:
        pos = y % len(seqList[index])
        lastAns = seqList[index][pos]
        print(lastAns)
