import random

n = random.choice(range(3, 21))
print(n)
result = []
for i in range(1, n - 1):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            result.append(i)
            result.append(j)
            break
print(*result)