# task 3
#
# Написати калькулятор з основними операціями(+, -, *, /)
#
# Користувач вводить два числа та арифметичну операцію
#
# Також можна додати перевірку для всіх задач з негативним сценарієм.

# Моя версія

# У всіх обчисленнях додала round аби уникнути занадто великої кількості знаків після коми.

# first_number = float(input("Enter first number: "))
# second_number = float(input("Enter second number: "))
# user_choice = input("Enter operation: \n + to add \n - to subtract \n * to multiply \n / to divide \n")
#
# if user_choice == "+":
#     result = round((first_number + second_number), 3)
#     print(f"{first_number} + {second_number} = {result}")
# elif user_choice == "-":
#     result = round((first_number - second_number), 3)
#     print(f"{first_number} - {second_number} = {result}")
# elif user_choice == "*":
#     result = round((first_number * second_number), 3)
#     print(f"{first_number} * {second_number} = {result}")
# elif user_choice == "/":
#     if second_number == 0:
#         print("Division by 0!")
#     else:
#         result = round((first_number / second_number), 3)
#         print(f"{first_number} / {second_number} = {result}")
# else:
#     print("Please, enter correct operation!")

# Покращена версія

# first_number = float(input("Enter first number: "))
# second_number = float(input("Enter second number: "))
# user_choice = input("Enter operation: \n + to add \n - to subtract \n * to multiply \n / to divide \n")
# result = None
#
# if user_choice == "+":
#     result = first_number + second_number
# elif user_choice == "-":
#     result = first_number - second_number
# elif user_choice == "*":
#     result = first_number * second_number
# elif user_choice == "/":
#     if second_number == 0:
#         print("Division by 0!")
#     else:
#         result = first_number / second_number
# else:
#     print("Please, enter correct operation!")
#
# print(f"{first_number} {user_choice} {second_number} = {round(result, 3)}")