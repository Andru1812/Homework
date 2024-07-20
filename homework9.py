numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in numbers:
    k = 0
    for j in range(1, i + 1):
        if i % j == 0:
            k += 1
        else:
            k = k
    if k == 2:
        primes.append(i)
    elif k > 2:
        not_primes.append(i)
print('Primes = ', primes, 'Not_primes = ', not_primes)