import random

max_value = 10
min_value = -10
numbers = []
new_numbers = []

n = int(input("Enter a number: "))

for i in range(n):
    numbers.append(random.randint(min_value, max_value))

print("Original list:", numbers)

negatives = [x for x in numbers if x < 0]

if negatives:
    max_negative = max(negatives)
    index = numbers.index(max_negative)
    new_numbers = [x ** 2 for x in numbers[:index]] + numbers[index:]
else:
    new_numbers = numbers[:]

print("Transformed list:", new_numbers)