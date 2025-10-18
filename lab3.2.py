import random

n = len("Ростислав")
m = len("Боднар")
max_value = 10
min_value = -10
matrix = [[random.randint(min_value, max_value) for _ in range(m)] for _ in range(n)]
new_numbers = []

print("Original matrix:")
for row in matrix:
    print(row)

max_negative = None
min_positive = None
max_neg_pos = None
min_pos_pos = None

for i in range(n):
    for j in range(m):
        if matrix[i][j] < 0:
            if (max_negative is None) or (matrix[i][j] > max_negative):
                max_negative = matrix[i][j]
                max_neg_pos = j
        elif matrix[i][j] > 0:
            if (min_positive is None) or (matrix[i][j] < min_positive):
                min_positive = matrix[i][j]
                min_pos_pos = j

if max_neg_pos is not None and min_pos_pos is not None:
    for i in range(n):
        matrix[i][max_neg_pos], matrix[i][min_pos_pos] = matrix[i][min_pos_pos], matrix[i][max_neg_pos]

print("\nTransformed matrix:")
for row in matrix:
    print(row)