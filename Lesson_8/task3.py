# 3- Створіть декоратор, який повертає результат функції,
# а також час за який вона виконана. Підсказка (для фіксації часу імпортуйте модуль time:  import time)

import time


def my_func_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() * 1000  # timer start, переводимо час в мілісекунди
        result = func(*args, **kwargs)
        end_time = time.time() * 1000  # timer end, переводимо час в мілісекунди
        func_time = end_time - start_time
        print(f"Result of the function: {result}; used time {func_time} milliseconds")
        return result

    return wrapper


@my_func_time
def sum_of_numbers(start, end):
    if start > end:
        end, start = start, end
    result = 0
    for i in range(start, end + 1):
        result += i
    return result


if __name__ == "__main__":
    try:
        sum_of_numbers(1, 1000000)

    except Exception as error:
        print(error)
