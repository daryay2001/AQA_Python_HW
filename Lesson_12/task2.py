# Створіть ітератор, який приймає послідовність і може перебирати значення в заданому діапазоні.
# CustomIterator(послідовність, початковий_індекс, кінцевий_індекс)

class CustomIterator:
    def __init__(self, sequence, start_index: int, stop_index: int):
        self.sequence = sequence
        self._start_index = start_index
        self._stop_index = stop_index

    def __iter__(self):
        return self

    def __next__(self):

        if self._start_index <= self._stop_index:
            if self._start_index < len(self.sequence):
                value = self.sequence[self._start_index]
                self._start_index += 1
                return value
            else:
                raise StopIteration
        else:
            raise StopIteration


if __name__ == '__main__':
    try:
        my_list = [1, 2, "Three", "Apple", True, 134.5]

        start = 0
        end = 2
        second_iter = CustomIterator(my_list, start, end)

        print(next(second_iter))
        print(next(second_iter))
        print(next(second_iter))
        print("______________________")

        my_sequence = [10, 20, 30, 40, 50]
        start_index = 3
        end_index = 1
        custom_iterator = CustomIterator(my_sequence, start_index, end_index)
        print(next(custom_iterator))
        print("______________________")

        start = 0
        end = 2
        my_iter = CustomIterator(my_list, start, end)
        print(next(my_iter))
        print(next(my_iter))
        print(next(my_iter))
        print(next(my_iter))

    except StopIteration as error:
        print("There is no more items between start and end.")
    except Exception as error:
        print(error)
