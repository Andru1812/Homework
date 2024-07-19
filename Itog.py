grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
g = {}
st = [0] * len(students)
for s in students:
    g[ord(s[0])] = s
for b in range(len(students)):
    st[b] = g.pop(max(g.keys()))
st = st[::-1]

balls = {}
for i in range(len(st)):
    bl = grades[i]
    s = 0
    for j in bl:
        s += j
    balls[st[i]] = s/len(bl)
print(balls)