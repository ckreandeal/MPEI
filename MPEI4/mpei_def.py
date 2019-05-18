# Список фунций для задания семинара 2

def is_min(curent_value, min_value):
    if curent_value < min_value:
        return True
    else:
        return False


def is_on_main(i, j):
    if i == j:
        return True
    else:
        return False

def create_matrix(n, m):
    import random
    a = []
    a = [0] * n
    for i in range(n):
        a[i] = [0] * m

    # Заполнение матриицы
    for i in range(n):
        for j in range(m):
            a[i][j] = random.randrange(-100, 100)
    return a

def search_min(arrey):
    min_value = arrey[0][0]
    for i in range(len(arrey)):
        for j in range(len(arrey)):
            if is_on_main(i,j) == True:
               if is_min(arrey[i][j], min_value) == True:
                   min_value = arrey[i][j]


    return min_value