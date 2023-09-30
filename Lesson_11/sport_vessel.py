from my_vessel import Vessel


class SportVessel(Vessel):
    """This class is the description of the sport vessel and its mandatory characteristics"""

    def __init__(self, name: str, year: int, imo: int, draft: int or float,
                 speed: int or float, material: str, motor_type: str):
        super().__init__(name, year, imo, draft, speed, material)

        self._motor_type = "GT-30"
        self.motor = motor_type

        self.sport_attr = "This is a sport vessel."
        self.entert_attr = "This vessel was build for entertainment."

    @property
    def motor(self):
        return self._motor_type

    @motor.setter
    def motor(self, new_motor: str):
        if isinstance(new_motor, str) and len(new_motor) >= 1:
            self._motor_type = new_motor

    def trade(self):
        print(f"Vessel {self._name} makes money by participating in competitions.")

    def vessel_info(self):
        super().vessel_info()
        print(f"{self._name} is a sport vessel. \nType of the motor is {self._motor_type}.")
