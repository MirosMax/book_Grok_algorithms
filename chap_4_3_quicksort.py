# Алгоритм быстрой сортировки с помощью рекурсии
import time
import random


def quicksort(list):
    if len(list) < 2:
        return list  # базовый случай - список из 1 или 0 элементов уже отсортированы
    else:
        base_el = list[0]  # выбираем базовый элемент
        more_base = [i for i in list[1:] if i >= base_el]  # формируем список элементов больше базового
        less_base = [i for i in list[1:] if i < base_el]  # формируем список элементов меньше базового
        return quicksort(less_base) + [base_el] + quicksort(more_base)


list_ = [random.randint(1, 1000) for i in range(1000)]

# start = time.time()
print(quicksort(list_))
# finish = time.time()
# time_quicksort = round(finish - start, 5)
