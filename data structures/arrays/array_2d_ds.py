#!/bin/python3

#https://www.hackerrank.com/challenges/2d-array

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)


max_sum = float("-inf")
for i in range(len(arr)-2):
    for j in range(len(arr[i])-2):
        local_sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j]+arr[i+2][j+1] + arr[i+2][j+2]
        if local_sum > max_sum:
            max_sum = local_sum

print(max_sum)