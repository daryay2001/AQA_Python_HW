from cargo_vessel import CargoVessel


class ContainerVessel(CargoVessel):
    """This class is the description of the container vessel and its mandatory characteristics"""

    def __init__(self, name: str, year: int, imo: int, draft: int or float, speed: int or float, material: str,
                 direction: str, container_capacity: int):
        super().__init__(name, year, imo, draft, speed, material, direction)
        self._container_capacity = 0
        self.capacity = container_capacity

        self.container_attr = "This is container vessel."
        self.cont_holds = ("The holds of the container vessels"
                           " have special cellular design to store the container properly.")
        self.teu = ("A TEU (twenty-foot equivalent unit) is a measure"
                    " of volume in units of twenty-foot long containers.")

    @property
    def capacity(self):
        return self._container_capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if isinstance(new_capacity, int) and new_capacity > 0:
            self._container_capacity = new_capacity

    def trade(self):
        super().trade()
        print(f"This vessel transports {self._container_capacity} TEU.")

    def vessel_info(self):
        super().vessel_info()
        print(f"container capacity: {self._container_capacity} TEU.")


if __name__ == '__main__':
    try:
        ever = ContainerVessel(name="Ever Golden", year=2015, imo=5555555, draft=20.8, speed=22.5,
                               material="steel", direction="Far East - Middle East", container_capacity=12450)
        ever.vessel_info()
        print(ever.get_imo("1234"))
        ever.trade()
        print(ever.teu)
    except Exception as error:
        print(error)
