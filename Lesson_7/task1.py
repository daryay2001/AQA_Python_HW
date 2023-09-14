# 1 - Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа
# від значення start до величини end включно. Якщо користувач задасть перше число більше,
# ніж друге, просто поміняйте їх місцями.

def sum_range(start, end):
    if start > end:
        start, end = end, start

    result = 0
    for i in range(start, end + 1):
        result += i

    return result


if __name__ == "__main__":
    try:
        print(sum_range(3, 7))
        print(sum_range(7, 3))
        print(sum_range(0, 0))
        print(sum_range(-2, 5))
        print(sum_range("apple", "sdfgg"))
        print(sum_range("abc", 5))

    except ValueError as error:
        print("Incorrect type of the variable")
    except Exception as error:
        print(error)
