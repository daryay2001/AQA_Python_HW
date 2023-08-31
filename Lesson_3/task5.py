# 5. (*) - за бажанням
# Додати перевірку введеної IP-адреси. Адреса вважається коректно заданою, якщо вона:
#
# складається з 4 чисел (а не літер чи інших символів)
# числа розділені точкою
# кожне число в діапазоні від 0 до 255 Якщо адреса неправильна,виводьте повідомлення: «Неправильна IP-адреса».
# Повідомлення "Неправильна IP-адреса" має виводитися лише один раз, навіть якщо кілька пунктів вище не виконані.
# Обмеження: завдання треба виконувати, використовуючи лише пройдені теми.

user_ip = input("Enter your ip: ").strip()
num_list = user_ip.split(".")

decision = None

if len(num_list) != 4:
    decision = "Incorrect IP-address"
else:
    for i in num_list:
        if not i.isdigit():
            decision = "Incorrect IP-address "
            break

        if int(i) < 0 or int(i) > 255:
            decision = "Incorrect IP-address "
            break
        else:
            decision = "IP-address is confirmed"

print(decision)

