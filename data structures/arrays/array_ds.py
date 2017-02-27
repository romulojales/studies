#!/bin/python3

#https://www.hackerrank.com/challenges/arrays-ds

#revert an array

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

for i in range(int(n/2)):
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
print(" ".join(map(str,arr)))
