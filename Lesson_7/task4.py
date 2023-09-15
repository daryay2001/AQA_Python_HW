# 4 - написати власну функцію map, використовуючи callback

test_list = ["2", 4, 25.8, True, None]
name_list = ["Alice", "Tom", "Harry", 23, False, None, "Nicolas"]


def do_str(my_list: list):
    str_list = []
    for i in my_list:
        if not isinstance(i, str):
            str_list.append(str(i))
        else:
            str_list.append(i)
    return str_list


def print_hello(names_list: list):
    for name in names_list:
        if isinstance(name, str):
            print(f"Hello, {name}")


def my_map(callback, sequence: list):
    return callback(sequence)


if __name__ == "__main__":
    try:
        print(my_map(do_str, test_list))
        my_map(print_hello, name_list)

    except Exception as error:
        print(error)
