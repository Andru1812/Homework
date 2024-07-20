import random
def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        mat_1 = []
        for j in range(m):
            mat_1.append(value)
        matrix.append(mat_1)
    return matrix

for i in range(3):
    n = random.choice(range(2, 15))
    m = random.choice(range(2, 15))
    value = input('Введите значение: ')
    mat_1 = get_matrix(n, m, value)
    print(mat_1)