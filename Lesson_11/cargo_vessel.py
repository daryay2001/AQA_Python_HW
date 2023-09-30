from my_vessel import Vessel


class CargoVessel(Vessel):
    """This class is the description of the cargo vessel and its mandatory characteristics"""
    def __init__(self, name: str, year: int, imo: int, draft: int or float,
                 speed: int or float, material: str, direction: str):
        super().__init__(name, year, imo, draft, speed, material)

        self._direction = "Far East"
        self.direction = direction

        self.cargo_vessel_attr = "This vessel can transport only cargo."
        self.holds = "This vessel has holds to store the cargo."

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, new_direction: str):
        if isinstance(new_direction, str) and len(new_direction) >= 2:
            self._direction = new_direction

    def trade(self):
        print(f"Cargo vessel {self._name} is trading now.")

    def vessel_info(self):
        super().vessel_info()
        print(f"This cargo vessel operates on the direction {self._direction}")


if __name__ == '__main__':
    try:
        peng = CargoVessel("Peng May", 2015, 4456789,
                           17.5, 18, "steel", "Far East - Middle East")
        peng.vessel_info()
        print(peng.get_imo("1234"))
        print(peng.holds)
        print(peng.cargo_vessel_attr)
        print(peng.info_attr)
    except Exception as error:
        print(error)
