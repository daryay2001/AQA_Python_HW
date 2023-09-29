from abc import ABC, abstractmethod


class Vessel(ABC):
    """This class is the description of the common vessel and its mandatory characteristics"""

    def __init__(self, name: str, year: int, imo: int, draft: int or float,
                 speed: int or float, material: str):
        self._name = "No name"
        self._year = 1999
        self.__imo = None
        self._draft = 10
        self._speed = 8
        self._material = "Steel"

        # encapsulation
        self.name = name
        self.year = year
        self.imo = imo
        self.draft = draft
        self.speed = speed
        self.material = material

        self.vessel_attr = "This is the vessel"
        self.info_attr = "All vessels have their imo number. It consists of 7 figures."

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if isinstance(new_name, str) and len(new_name) >= 2:
            self._name = new_name

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year: int):
        if isinstance(new_year, int) and 1929 <= new_year <= 2023:
            self._year = new_year

    @property
    def imo(self):
        return self.__imo

    @imo.setter
    def imo(self, imo_number: int):
        if isinstance(imo_number, int) and 1000000 <= imo_number <= 9999999:
            self.__imo = imo_number

    @property
    def draft(self):
        return self._draft

    @draft.setter
    def draft(self, new_draft: int or float):
        if isinstance(new_draft, int) or isinstance(new_draft, float) and 2 <= new_draft <= 30:
            self._draft = new_draft

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed: int or float):
        if isinstance(new_speed, int) or isinstance(new_speed, float) and 8 <= new_speed <= 35:
            self._speed = new_speed

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, new_material: str):
        if isinstance(new_material, str) and len(new_material) >= 2:
            self._material = new_material

    def vessel_info(self):
        print(f"Public info about vessel:\n"
              f"name: {self._name} \nyear: {self._year} \ndraft: {self._draft} m \nspeed: {self._speed} knots"
              f"\nmaterial: {self._material} ")

    def get_imo(self, your_key):
        if your_key == "1234":
            return f"imo: {self.__imo}"
        else:
            return f"imo: *******"

    @abstractmethod
    def trade(self):
        pass



