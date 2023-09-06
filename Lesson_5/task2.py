# 2 - Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу,
# що складається з числа, оператора (як мінімум * і /) та іншого числа,
# розділених пробілом (наприклад, 2 * 5).
#
# Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.
# Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError
# Якщо введені числа не можуть бути float спіймайте ValueError
# Також ловіть помилку при діленні на 0
# В кожній спійманій помилці друкуйте пояснення, що пішло не так
# За допомогою циклів (while + counter) або (for + in range) надайте три спроби скористуватись калькулятором,
# якщо введені не вірні дані
# Використати всі блоки try, except, else, finally. В finally можна надрукувати за скільки спроб виконавлась формула
# Результат виконання формули - float число з двома знаками після крапки

class WrongOperatorError(Exception):
    pass


try:
    user_formula = input("Enter your expression: ").strip()
    elem_list = user_formula.split()

    num1 = float(elem_list[0])
    operator = elem_list[1]
    num2 = float(elem_list[2])
    result = None

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError
        else:
            result = num1 / num2
    else:
        raise WrongOperatorError("Wrong operator was entered!")

    print(f"{num1} {operator} {num2} = {result}")

except Exception as error:
    print(error)
else:
    pass
finally:
    pass
