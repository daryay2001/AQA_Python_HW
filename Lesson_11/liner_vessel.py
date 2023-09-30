from passenger_vessel import PassengerVessel


class Liner(PassengerVessel):
    """This class is the description of the liners and its mandatory characteristics"""

    def __init__(self, name: str, year: int, imo: int, draft: int or float, speed: int or float, material: str,
                 passenger_capacity: int, region: str):
        super().__init__(name, year, imo, draft, speed, material, passenger_capacity)
        self._region = "Secret region"
        self.region = region

        self.liner_attr = "This is a cruise vessel."
        self.ticket_attr = "You should buy ticket to go on boar."

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, new_region: str):
        if isinstance(new_region, str) and len(new_region) >= 2:
            self._region = new_region

    def vessel_info(self):
        super().vessel_info()
        print(f"This vessel operates in the {self._region} region")

    def trade(self):
        super().trade()
        print(f"{self._name} vessel on the cruise.")

    def __transport_passengers(self):
        print(f"Vessel {self._name} can transport {self._passenger_capacity} passengers.")

    def __cruise_region(self):
        print(f"This vessel makes money by operating in {self._region} region.")

    def be_on_cruise(self):
        self.__transport_passengers()
        self.__cruise_region()


if __name__ == '__main__':
    try:
        queen = Liner("Queen Elizabeth", 1940, 3456789, 12,
                      28, "wood and steel", 2283, "Northern Europe")
        queen.vessel_info()
        print(queen.get_imo("1234"))
        queen.trade()
        queen.be_on_cruise()
        print(queen.ticket_attr)
        print(queen.liner_attr)
    except Exception as error:
        print(error)
