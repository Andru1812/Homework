def get_multiplied_digits(number):
    if number == '':
        return 1
    elif len(number) > 1:
        m = int(number[-1])
        return m * get_multiplied_digits(number[:-1])
    else:
        return int(number)

set_number = input('Введите число')
while not set_number.isdigit():
    set_number = input('Введите число заново')

print(get_multiplied_digits(set_number))