#https://www.hackerrank.com/challenges/crush

N, M = map(int, input().strip().split())

n = [0]*N

max_value = -1
for _ in range(M):
    a, b, k = map(int, input().strip().split())
    for i in range(a-1, b):
        n[i] += k
        if n[i] > max_value:
            max_value = n[i]

print(max_value)
