def calculate_structure_sum(list_0):
    if type(list_0) == tuple or type(list_0) == set:
        list_0 = [*list_0]
    elif type(list_0) == dict:
        list_0 = [*list_0.items()]
    i = 0
    k = len(list_0)
    while i != k:
        b1 = type(list_0[i]) == list
        b2 = type(list_0[i]) == tuple
        b3 = type(list_0[i]) == set
        b4 = type(list_0[i]) == dict
        if b1 or b2 or b3:
            col = list_0.pop(i)
            list_0 = [*list_0, *col]
        elif b4:
            col = list_0.pop(i)
            list_0 = [*list_0, *col.items()]
        else:
            i += 1
        k = len(list_0)
    s = 0
    for j in list_0:
        if type(j) == int or type(j) == float:
            s += j
        elif type(j) == str:
            s += len(j)
    return s

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)