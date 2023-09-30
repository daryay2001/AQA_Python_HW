# 2 - Create a class with a description of the worker. Any worker or employees.
from random import randrange


class Employee:
    """This class is the description of our employees"""

    def __init__(self, name: str, age: int, company: str, position: str, salary: int or float):
        self._name = "No name"  # protected
        self.__age = 18  # private
        self._company = "The best company"  # protected
        self.__position = "Secret position"  # private
        self.__salary = 0
        self.__security_data = {"passport": randrange(10 ** 8, 10 ** 9),  # рандомне дев`ятизначне число
                                "code": randrange(10 ** 9, 10 ** 10),  # рандомне десятизначне число
                                "access key": 125734}
        self.name = name  # Застосували інкапсуляцію
        self.age = age
        self.company = company
        self.position = position
        self.salary = salary

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if isinstance(new_name, str) and len(new_name) >= 2:
            self._name = new_name
        else:
            print("Incorrect name")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age: int):
        if isinstance(new_age, int) and 100 >= new_age >= 18:
            self.__age = new_age
        else:
            print("Incorrect age")

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, new_company: str):
        if isinstance(new_company, str) and len(new_company) >= 2:
            self._company = new_company
        else:
            print("Incorrect company")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position: str):
        if isinstance(new_position, str) and len(new_position) >= 2:
            self.__position = new_position
        else:
            print("Incorrect position")

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary: int or float):
        if isinstance(new_salary, int) or isinstance(new_salary, float) and new_salary > 0:
            self.__salary = new_salary

    @staticmethod
    def short_information():
        print("All employees are adults")

    def show_info(self):
        """This method will show you information about our employees"""
        print(f"Employee name: {self._name}, \nage: {self.__age}, \ncompany: {self._company},"
              f" \nposition: {self.__position}")

    def __str__(self):
        """This method shows the result as if you had applied the str function to an instance of the class"""
        return f"{self._name}, {self.__age}, {self._company}, {self.__position}, {self.__salary}"

    def __repr__(self):
        """This method shows the result as if you had applied the representation function to an instance of the class"""
        return f"Employee({self._name}, {self.__age}, {self._company}, {self.__position}, {self.__salary})"

    def get_secret_info(self, your_key: int):
        if your_key == self.__security_data["access key"]:
            return self.__security_data
        else:
            secret_data = {key: "*******" for key, value in self.__security_data.items()}
            return f"Info only for admin, \n{secret_data}"

    def _make_notes(self):
        print(f"{self._name} is making important notes!")

    def __nda_info(self):
        print(f"{self._name} is working with NDA info!")

    def work_with_documents(self):
        """This method will show you that employee is making notes and working with NDA information"""
        self._make_notes()
        self.__nda_info()

    @classmethod
    def empl_sertificate(cls, name: str, age: int, company: str, position: str,
                         salary: int or float, new_certificate: str = "No certificate"):
        """This method will show employee certificate"""
        obj_ = cls(name, age, company, position, salary)
        if isinstance(new_certificate, str) and len(new_certificate) > 2:
            obj_.certificate = new_certificate
        else:
            obj_.certificate = "No certificate"
        return obj_


if __name__ == '__main__':
    try:
        yuki = Employee("Yuki Sato", 22, "Sony", "Engineer", 2200)
        yuki.show_info()
        Employee.short_information()
        yuki.work_with_documents()
        yuki._make_notes()
        print(yuki.get_secret_info(125734))
        print(yuki.get_secret_info(222222))
        print(str(yuki))
        print(repr(yuki))
        print("-----------------------------")

        sakura = Employee.empl_sertificate("Sakura Yoshimura", 34, "Sony",
                                           "Team lead engineer", 5700, "Employee of the year")
        print(sakura.certificate)
        sakura.show_info()
        print("------------------------------")

        kayaba = Employee.empl_sertificate(name="Kayaba Akihiko", age=40, company="Sony",
                                           position="game-developer", salary=4300, new_certificate="A")
        print(f"Kayaba have: {kayaba.certificate}")

        print("-----------------------------")

        hikaru = Employee(name=True, age=128, company="E", position="N", salary=-500)
        hikaru.show_info()

    except Exception as error:
        print(error)

