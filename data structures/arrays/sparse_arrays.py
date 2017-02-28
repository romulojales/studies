#https://www.hackerrank.com/challenges/sparse-arrays

number_of_strings = int(input().strip())
strings = []
for _ in range(number_of_strings):
    strings.append(input().strip())
number_of_queries = int(input().strip())

for _ in range(number_of_queries):
    query = input().strip()
    occurs = 0
    for string in strings:
        if string == query:
            occurs += 1
    print(occurs)
