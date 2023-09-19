# 1- Створіть декоратор, який виводить в консоль назву викликаної функції.
# Наприклад, створіть пару функцій для арифметичних операцій підсумовування та множення.
# Під час виклику цих функцій має бути повернутий результат операції, а ім’я викликаної функції
# має відображатися на консолі разом із результатом. Маленька підказка (__name__)

def func_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Name of the function: {func.__name__}, result: {result}")
        print("________________")
        return result

    return wrapper


@func_name
def my_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError as error:
        print(error)
    except Exception as error:
        print(error)


@func_name
def my_sum(a, b):
    try:
        result = a + b
        return result
    except Exception as error:
        print(error)


@func_name
def my_mult(a, b):
    try:
        result = a * b
        return result
    except Exception as error:
        print(error)


@func_name
def my_sub(a, b):
    try:
        result = a - b
        return result
    except Exception as error:
        print(error)


if __name__ == "__main__":
    my_sum(5, 2)
    my_sum(2, "dsfdj")
    my_sub(7, 8)
    my_sub("Hello", 25)
    my_mult(7, 6)
    my_division(15, 5)
    my_division(5, 0)

