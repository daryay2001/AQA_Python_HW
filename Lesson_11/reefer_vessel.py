from cargo_vessel import CargoVessel


class Reefer(CargoVessel):
    """This class is the description of the reefer vessel and its mandatory characteristics"""

    def __init__(self, name: str, year: int, imo: int, draft: int or float,
                 speed: int or float, material: str, direction: str, cargo: str, capacity: int):
        super().__init__(name, year, imo, draft, speed, material, direction)

        self._cargo = "Meat"
        self._capacity = 0

        self.cargo = cargo
        self.capacity = capacity

        self.reefer_attr = "This vessel can carry goods that need special temperature control."
        self.temperature = "This vessel can change temperature in the holds."

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, new_cargo: str):
        if isinstance(new_cargo, str) and len(new_cargo) >= 2:
            self._cargo = new_cargo

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity: int):
        if isinstance(new_capacity, int) and new_capacity > 0:
            self._capacity = new_capacity

    def vessel_info(self):
        super().vessel_info()
        print("type: Reefer")
        print(f"capacity: {self._capacity} tons")

    def trade(self):
        super().trade()
        print(f"Vessel {self._name} can carry {self._capacity} tons of {self._cargo}")

    @staticmethod
    def keep_safe():
        print(f"This vessel will keep safe special goods.")


if __name__ == '__main__':
    try:
        star = Reefer("Cold Star", 2001, 4545454, 17.8, 15.6, "steel",
                      "Middle East", "Fish", 12500)
        star.vessel_info()
        print(star.get_imo("1234"))
        star.keep_safe()
    except Exception as error:
        print(error)
