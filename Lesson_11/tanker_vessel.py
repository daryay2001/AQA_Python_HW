from cargo_vessel import CargoVessel


class Tanker(CargoVessel):
    """This class is the description of the tanker vessel and its mandatory characteristics"""

    def __init__(self, name: str, year: int, imo: int, draft: int or float,
                 speed: int or float, material: str, direction: str, liquid_type: str, capacity: int):
        super().__init__(name, year, imo, draft, speed, material, direction)

        self._liquid_type = "Crude oil"
        self._capacity = 0

        self.liquid = liquid_type
        self.capacity = capacity

        self.tanker_attr = "This is a tanker vessel."
        self.liquid_attr = "Tanker can carry just liquids."

    @property
    def liquid(self):
        return self._liquid_type

    @liquid.setter
    def liquid(self, new_liquid: str):
        if isinstance(new_liquid, str) and len(new_liquid) >= 2:
            self._liquid_type = new_liquid

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity: int):
        if isinstance(new_capacity, int) and new_capacity > 0:
            self._capacity = new_capacity

    def vessel_info(self):
        super().vessel_info()
        print(f"Capacity of the vessel is {self._capacity} barrels.")
        print(f'Type of the vessel {self._name} is tanker.')

    def trade(self):
        super().trade()
        print(f"This vessel can carry {self._capacity} barrels of {self._liquid_type} per voyage.")

    def __loading(self):
        print(f"Turn on pump to start {self._liquid_type} loading.")

    def __go_to_pod(self):
        print(f"Vessel {self._name} is going to the port of discharging.")

    def __discharging(self):
        print(f"Turn on pump to start {self._liquid_type} discharging.")

    def transport_liquid(self):
        self.__loading()
        self.__go_to_pod()
        self.__discharging()


if __name__ == '__main__':
    try:
        star = Tanker("Green Star", 2001, 4545454, 17.8, 15.6, "steel",
                      "Middle East", "Oil", 50000)

        star.transport_liquid()
        star.vessel_info()
    except Exception as error:
        print(error)
