# 1 - Дано список str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# Лише за допомогою функцій map, lambda, zip створити та надрукувати словник квадратів цих чисел.
# Очікуваний результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

# v1

str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
int_list = list(map(int, str_list))
sqr_list = list(map(lambda x: x ** 2, int_list))

my_dict = dict(zip(int_list, sqr_list))

print(my_dict)

# v2

res_dict = dict(zip(map(int, str_list), map(lambda x: x ** 2, map(int, str_list))))
print(res_dict)


