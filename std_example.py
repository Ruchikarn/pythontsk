import math

data = [4, 10, 14, 13, 14]
N = len(data)
mean = sum(data) / N
total = 0
for x in data:
    total += (x - mean) ** 2
std = math.sqrt(total / N)
print('Std', std)
print('Mean', mean)