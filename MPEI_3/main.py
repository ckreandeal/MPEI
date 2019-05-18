# Семинар 1. Задание 3.

# Step 1. Зададим размерность матрицы a. n - колиичество строк m - количество столбцов

n = int(input('Введите количество строк матрицы'))
m = int(input('Введите количество столбцов матрицы'))

# Step 2. Создадим пустую матницу n x m
a = []

a = [0] * n
for i in range(n):
    a[i] = [0] * m

# Step 3. Пользовательское заполнение матриицы
for i in range(n):
    for j in range (m):
        a[i][j] = int(input('Введиите значеение элемента a[{},{}]'.format(i,j)))

# Step 4. Вывод матрицы
for i in a:
    print(i)


# Step 5. Поиск нулевых элементов матрицы
index_list = []

for i in range(n):
    for j in range (m):
        if a[i][j] == 0:
            index_list.append('{},{}'.format(i,j))

# Step 6. Выводим список индексов нулевых элементов
print('Список индексов нулевых элементов матрицы a {}'.format(index_list))
