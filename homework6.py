my_dict = {'Andrey': 'student', 'Maxim': 'teacher', 'Anton': 'programmer'}
print(my_dict)
my_dict['Sergey'] = 'cabbie'
print(my_dict['Maxim'], my_dict['Sergey'])
my_dict.update({'Denis': 'security', 'Artem': 'cashier'})
print(my_dict.pop('Maxim'))
print(my_dict)

my_set = {0, False, True, 1, 1, True, 2, 3, 4, 5, 5, 6, 7, 2, '8', 9, 0, False}
print(my_set)
for i in range(2):
    j = i + 10
    my_set.add(j)
my_set.discard(5)
print(my_set)