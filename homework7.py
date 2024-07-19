def proverka(chislo):
    if chislo.isdigit():
        chislo = int(chislo)
        return chislo
    else:
        chislo = input('Введите заново')
        proverka(chislo)

first_v = input('Введите первое число')
first = proverka(first_v)

second_v = input('Введите второе число')
second = proverka(second_v)

third_v = input('Введите третье число')
third = proverka(third_v)

chl = {first, second, third}
if len(chl) == 1:
    print(3)
elif len(chl) == 2:
    print(2)
else:
    print(0)