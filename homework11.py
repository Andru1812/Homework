import random
calls = 0
def count_colls():
    global calls
    calls += 1

def string_info(string_1):
    cortege = (len(string_1), string_1.upper(), string_1.lower())
    count_colls()
    return cortege

def is_contains(string_2, list_1):
    proverka = False
    for i in range(len(list_1)):
        if string_2.upper() == list_1[i].upper():
            proverka = True
            break
    count_colls()
    return proverka

k_1 = random.choice(range(3, 26))
for j_1 in range(k_1):
    list_0 = ['Andrey', 'Urban', 'Sergey', 'Anton', 'Vladimir', 'Boris', 'Georgiy', 'Denis']
    string_1 = input('Введите строку 1 ')
    si = string_info(string_1)
    print(*si)

print('')
k_2 = random.choice(range(3, 26))
for j_2 in range(k_2):
    string_2 = input('Введите строку 2 ')
    ic = is_contains(string_2, list_0)
    print(ic)

print('')
print('Calls = ', calls)