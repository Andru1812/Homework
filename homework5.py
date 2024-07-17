immutable_var = (0, True, '2 3', [4, 5])
print(immutable_var)
# immutable_var[2] = 3 # невозможно напрямую изменить элементы кортежа
# но если какой-то элемент кортежа изменяем сам по себе (например список), то можно произвести изменения внутри самого элемента
immutable_var[3][1] = 6
print(immutable_var)

mutable_list = [False, 1, '10', [11, 100]]
mutable_list[1] = True
mutable_list[0] = 0
print(mutable_list)