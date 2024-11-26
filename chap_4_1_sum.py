# Написать код для рекурсировного суммирования списка, на основе базового случая
# Базовый случай здесь это когда длина списка = 0


def summator(l):
    if len(l) == 0:
        return 0
    else:
        return l.pop() + summator(l)


list_ = [1, 5, 9, 2, 1, 5, 7]

print(summator(list_))