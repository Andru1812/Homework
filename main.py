#1st program
print((9**0.5)*5)

#2nd program
print(9.99 > 9.98 and 1000 != 1000.1)

#3rd program
x1 = '1234'
x2 = '5678'
print(int(x1[1] + x1[2]) + int(x2[1] + x2[2]))

#4th program
y1 = '13.42'
y2 = '42.13'
r1 = y1[::-1]
r2 = y2[::-1]
def drob(dr):
    i = 0
    c = ''
    while dr[i] != '.':
        c += dr[i]
        i += 1
    return c
y1 = drob(y1)
y2 = drob(y2)
r1 = drob(r1)
r2 = drob(r2)
r1 = r1[::-1]
r2 = r2[::-1]
print(y1 == r2 or y2 == r1)