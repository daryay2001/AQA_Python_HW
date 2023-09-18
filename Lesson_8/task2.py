# 2- Створіть функцію, яка може повертати квадрати парних чисел у діапазоні
# від 0 до 1000000000 включно. Рішення має працювати і не фрізити комп’ютер.

def square_of_even_num(first_num, last_num):
    if first_num > last_num:
        first_num, last_num = last_num, first_num

    sqr_num = first_num if first_num % 2 == 0 else first_num + 1

    while sqr_num <= last_num:
        yield sqr_num ** 2
        sqr_num += 2 # переходимо одразу до наступного парного числа, щоб знов не перевіряти


my_gen_sqr = square_of_even_num(1, 10)
# my_gen_sqr = square_of_even_num(10, 1)

for i in my_gen_sqr: # Перевірка на малому ренджі
    print(i)

big_sqr_gen = square_of_even_num(0, 1000000000) # Рішення комп не фрізить, проте дуже довго рахує, більш ніж 30хв

for num in big_sqr_gen:
    print(num)
