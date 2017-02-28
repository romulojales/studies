#https://www.hackerrank.com/challenges/array-left-rotation

length, rotations = map(int, input().strip().split())
array = list(map(int, input().strip().split()))
displacement = rotations % length

lower = []
for i in range(displacement, length):
    lower.append(array[i])

upper = []

for i in range(displacement):
    upper.append(array[i])
array = lower + upper

print(" ".join(map(str, array)))

## or

array = array[displacement:] + array[:displacement]