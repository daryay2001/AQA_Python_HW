# 1 -
#
# Опишіть об’єкт «Поїзд». Клас повинен містити поля та метод для додавання вагонів
# (необхідно додати об’єкти та екземпляри класу вагонів). Опишіть клас Вагон разом із поїздом.
# Вагон повинен містити список пасажирів і дозволяти додавати пасажирів.
# У Вагоні може бути наприклад не більше 10 пасажирів.
# Під час використання функції len у вагоні я хочу бачити кількість пасажирів.
# Використовуючи len у поїзді, я хочу бачити список вагонів без локомотива.
# Кожен вагон повинен мати номер.
# Під час друку вагона на консолі я хочу бачити наступне «[n]», де n — номер вагона.
#
# Реалізуйте друк потяга із завдання 2.
# Під час друку потяга вагони та локомотив мають відображатися на консолі у такому форматі:
#
# <=[HEAD]-[1]-[2]-[3]-[4]-[...]
#

class Wagon:
    """This class will describe passenger wagon of the common train."""

    def __init__(self, number: int):
        self._number = 0
        self.passengers = []

        self.number = number

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, new_number: int):
        if isinstance(new_number, int) and new_number > 0:
            self._number = new_number

    def add_passenger(self, passenger_name: str):
        if isinstance(passenger_name, str) and len(self.passengers) < 10:
            self.passengers.append(passenger_name)
            print(f"Hello, passenger {passenger_name}. Your wagon is {self._number}")
        else:
            print(f"This wagon {self._number} is filled, sorry.")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f"[{self._number}]"


class Train:
    """This class will describe common train and sequence of its wagons.
     Please, admit, that wagon numbers not always should be placed consecutively,
      because its normal practice in the real life."""

    def __init__(self):
        self.wagons = []

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        if not self.wagons:
            return "<=[HEAD]"

        wagon_numbers = "-".join([f"[{wagon._number}]" for wagon in self.wagons])
        return f"<=[HEAD]-{wagon_numbers}"


if __name__ == '__main__':
    try:
        my_train = Train()

        first_wagon = Wagon(1)
        first_wagon.add_passenger("Alice")
        first_wagon.add_passenger("Holly")
        first_wagon.add_passenger("Harry Potter")
        first_wagon.add_passenger("Draco Malfoy")
        first_wagon.add_passenger("Hermione Granger")
        first_wagon.add_passenger("Ron Weasley")
        first_wagon.add_passenger("Lord Voldemort")
        first_wagon.add_passenger("Stranger")
        first_wagon.add_passenger("Frodo")
        first_wagon.add_passenger("Sam")
        first_wagon.add_passenger("Gollum")
        print("______________________________")

        second_wagon = Wagon(2)
        second_wagon.add_passenger("Severus Snape")
        second_wagon.add_passenger("James Potter")
        second_wagon.add_passenger("Lilly Potter")
        print("______________________________")

        third_wagon = Wagon(3)
        third_wagon.add_passenger("Spider-Man")
        third_wagon.add_passenger("Batt-Man")
        print("______________________________")

        fourth_wagon = Wagon(4)
        fourth_wagon.add_passenger("Snow White")
        fourth_wagon.add_passenger("Ariel")
        print("______________________________")

        print(f"Length of the wagon 1 is {len(first_wagon)}")
        print(f"Length of the wagon 2 is {len(second_wagon)}")
        print(f"Length of the wagon 3 is {len(third_wagon)}")
        print(f"Length of the wagon 4 is {len(fourth_wagon)}")

        my_train.add_wagon(first_wagon)
        my_train.add_wagon(second_wagon)
        my_train.add_wagon(third_wagon)
        my_train.add_wagon(fourth_wagon)

        print(f"See the full train: {my_train}")

        print("______________________________")
        print(f"length of the first wagon is: {len(first_wagon)}")
        print(f"length of the my train is: {len(my_train)}")

    except Exception as error:
        print(error)

