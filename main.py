def total(a=5, *golova, **phone_book):
    print('a', a)
    # проход по всем элементам кортежа
    for single_item in golova:
        print('single_item', single_item)

    #проход по всем элементам словаря
    for firsct_part, second_part in phone_book.items():
        print(firsct_part,second_part)

total(10, 1, 2, 3, 4, 'a', Jack=1123, John=2231, Inge=1560)