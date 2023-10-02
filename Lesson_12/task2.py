# Створіть ітератор, який приймає послідовність і може перебирати значення в заданому діапазоні.
# CustomIterator(послідовність, початковий_індекс, кінцевий_індекс)

class CustomIterator:
    def __init__(self, sequence, start_index: int, stop_index: int):
        self.sequence = sequence
        self._start_index = 0
        self._stop_index = 1

        self.start = start_index
        self.stop = stop_index

        if self._start_index > self._stop_index:
            self._start_index, self._stop_index = self._stop_index, self._start_index

        self.current_index = self._start_index

    @property
    def start(self):
        return self._start_index

    @start.setter
    def start(self, new_start: int):
        if isinstance(new_start, int) and new_start >= 0:
            self._start_index = new_start

    @property
    def stop(self):
        return self._stop_index

    @stop.setter
    def stop(self, new_stop: int):
        if isinstance(new_stop, int) and new_stop >= 0:
            self._stop_index = new_stop

    def __iter__(self):
        return self

    def __next__(self):

        if self.current_index <= self._stop_index:
            if self.current_index < len(self.sequence):
                value = self.sequence[self.current_index]
                self.current_index += 1
                return value
            else:
                raise StopIteration
        else:
            raise StopIteration


if __name__ == '__main__':
    try:
        my_list = [1, 2, "Three", "Apple", True, 134.5]

        start = 2
        end = 0
        second_iter = CustomIterator(my_list, end, start)

        print(next(second_iter))
        print(next(second_iter))
        print(next(second_iter))
        print("______________________")

        my_sequence = [10, 20, 30, 40, 50]
        start_index = 3
        end_index = 1
        custom_iterator = CustomIterator(my_sequence, start_index, end_index)
        for value in custom_iterator:
            print(value)
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
