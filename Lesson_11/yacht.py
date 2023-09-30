from sport_vessel import SportVessel


class Yacht(SportVessel):
    """This class is the description of the yacht and its mandatory characteristics"""

    def __init__(self, name: str, year: int, imo: int, draft: int or float, speed: int or float, material: str,
                 motor_type: str, crew: int):
        super().__init__(name, year, imo, draft, speed, material, motor_type)

        self._crew = 5
        self.crew = crew

        self.yacht_attr = "This is yacht and it participates in reggatas."
        self.crew_attr = "You could be a part of crew just if you have special certificate."

    @property
    def crew(self):
        return self._crew

    @crew.setter
    def crew(self, new_crew: int):
        if isinstance(new_crew, int) and new_crew > 0:
            self._crew = new_crew

    def trade(self):
        super().trade()
        print(f"The competition called reggata. Hope {self._name} will be the winner!")

    def vessel_info(self):
        super().vessel_info()
        print(f"Crew number: {self._crew}")

    def be_winner(self):
        print(f"Vessel {self._name} is a winner!")

