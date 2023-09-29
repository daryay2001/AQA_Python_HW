from my_vessel import Vessel


class PassengerVessel(Vessel):
    """This class is the description of the passenger vessel and its mandatory characteristics"""

    def __init__(self, name: str, year: int, imo: int, draft: int or float,
                 speed: int or float, material: str, passenger_capacity: int):
        super().__init__(name, year, imo, draft, speed, material)
        self._passenger_capacity = 0
        self.capacity = passenger_capacity

        self.passenger_attr = "This vessel can transport only passengers."
        self.cabins = "This vessel has cabins for the passengers."

    @property
    def capacity(self):
        return self._passenger_capacity

    @capacity.setter
    def capacity(self, new_capacity: int):
        if isinstance(new_capacity, int) and new_capacity >= 1:
            self._passenger_capacity = new_capacity

    def trade(self):
        print(f"Passenger vessel {self._name} is trading now.")

    def vessel_info(self):
        super().vessel_info()
        print(f"passenger capacity: {self._passenger_capacity}")


if __name__ == '__main__':
    try:
        sunrise = PassengerVessel("Sunrise", 2012, 7654321,
                                  10.5, 17.8, "steel", 5400)

        sunrise.vessel_info()
        print(sunrise.get_imo("1234"))
        print(sunrise.cabins)
        print(sunrise.passenger_attr)
    except Exception as error:
        print(error)
