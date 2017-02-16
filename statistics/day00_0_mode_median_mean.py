"""Find the mean, median and mode of a given set of numbers"""
from collections import defaultdict

amount_of_numbers = int(input())

numbers = sorted(map(int, input().split()))

#mean
mean = sum(numbers)/amount_of_numbers


#median
middle = int(amount_of_numbers/2)
if amount_of_numbers % 2:
    median = numbers[middle]
else:
    median = (numbers[middle] + numbers[middle-1])/2

#mode
mode = 0

seem = {}

for i in numbers:
    seem[i] = seem.get(i,0) + 1

most_common = 0
for number, repetitions in seem.items():
    if repetitions == most_common and mode > number:
        mode = number
    elif repetitions > most_common:
        most_common = repetitions
        mode = number

#results
print(round(mean, 1))
print(round(median,1))
print(round(mode,1))
