from  mpei_def import create_matrix, search_min, is_on_main, is_min


a = create_matrix(7,7)
b = create_matrix(5,5)

for i in range(len(a)):
    print(a[i])

print()


for i in range(len(b)):
    print(b[i])



a_min =  search_min(a)
b_min = search_min(b)


print()
print('Миинимальное значеениее на главной диагонали матриицы а (7x7) равно {}'.format(a_min))

print('Миинимальное значеениее на главной диагонали матриицы b (9x9) равно {}'.format(b_min))
