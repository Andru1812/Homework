def single_root_words(root_word, *other_words, txt='Однокоренные слову'):
    same_words = []
    for i in other_words:
        if i.upper().count(root_word.upper()) == 1 or root_word.upper().count(i.upper()) == 1:
            same_words.append(i)
    return f'{txt} {root_word}: {same_words}'

r_w = input('Введите слово')

o_w = ''
other_words = []
print('Введите набор слов. Для окончания введите 0')
while True:
    if o_w == '0':
        break
    o_w = input()
    other_words.append(o_w)
print(single_root_words(r_w, *other_words))