def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(a = 5, b = 'hello')
print_params()
print_params(c = False)
print_params(a = 0, b = 'world', c = False)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [False, 1, '2']
values_dict = {'a': '0', 'b': True, 'c': 2}

print()
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [0, '1']

print()
print_params(*values_list_2, 42)