# Написать алгоритм деления участка земли на равные квадраты с максимальной стороной
# Базовый случай - когда стороны кратны друг другу

def ferma(a, b):
    if b % a == 0 or a % b == 0:
        return min(a, b)
    else:
        if b > a:
            b -= a
        else:
            a -= b
        return ferma(a, b)


a = 640
b = 1680

print(ferma(a, b))