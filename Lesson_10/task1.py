# 1 - Create a class describing any company. For example, Toshiba or Apple
class SanrioCompany:
    """This class is the description of the japanese company Sanrio"""
    COMPANY = "Sanrio"

    def __init__(self, specialization: str):
        self._specialization = "No specialization"  # protected
        self.specializaton = specialization  # Застосували інкапсуляцію
        self.__employees = []  # private
        self.__charactes = []  # private

    @property
    def specializaton(self):
        return self._specialization

    @specializaton.setter
    def specializaton(self, specialization: str):
        if isinstance(specialization, str):
            self._specialization = specialization
        else:
            print("Value should be string type")

    @staticmethod
    def philosophy():
        """This method tells you about our corporation philosophy"""

        print("We aim to achieve our corporate philosophy of everyone getting along together"
              "\nby creating smiles one person at a time and spreading the circle of happiness even further afield.")

    def add_character(self, character: str):
        """This method will help you to add characters to the characters list"""
        if isinstance(character, str) and character in self.__charactes:
            print("Character is already added")
        elif isinstance(character, str):
            self.__charactes.append(character)
            print(f"Character is successfully added: {character}")
        else:
            print("Enter only string values")

    def remove_character(self, character: str):
        """This method will help you to remove characters from the characters list"""
        if character in self.__charactes:
            self.__charactes.remove(character)
        else:
            print(f"There is no such character: {character}, sorry =(")

    def add_employee(self, employee: str):
        """This method will help you to add employees to the employees list"""
        if isinstance(employee, str) and employee in self.__employees:
            print("Employee is already added")
        elif isinstance(employee, str):
            self.__employees.append(employee)
            print(f"Employee is successfully added: {employee}")
        else:
            print("Enter only string values")

    def remove_employee(self, employee: str):
        """This method will help you to remove employees from the employees list"""
        if employee in self.__employees:
            self.__employees.remove(employee)
        else:
            print(f"There is no such employee: {employee}, sorry =(")

    def show_info(self):
        """This method will show you information
                about Sanrio company (company name, specialization, characters and employees)"""
        print(f"Name of our pretty company is: {SanrioCompany.COMPANY}")
        print(f"Our specialization is: {self._specialization}")
        print("Enjoy our cute characters: ")
        for character in self.__charactes:
            print(character)
        print("---------------------------------")
        print("Please, meet our employees: ")
        for employee in self.__employees:
            print(employee)
        print("---------------------------------")


if __name__ == '__main__':
    try:
        sanrio = SanrioCompany("Production of popular cute and adorable characters")
        sanrio.philosophy()
        print("-------------------------")

        sanrio.add_character("Hello Kitty")
        sanrio.add_character("Kuromi")
        sanrio.add_character("My Melody")
        sanrio.add_character("Keroppy")
        sanrio.add_character(123)

        sanrio.add_employee("Yuki Hoshimura")
        sanrio.add_employee("Katty Smith")
        sanrio.add_employee("Sakura Oshizuki")
        sanrio.add_employee(True)
        print("-----------------------------")
        sanrio.show_info()

        sanrio.remove_character("Keroppy")
        sanrio.remove_character("Cat")
        sanrio.remove_employee("Katty Smith")
        sanrio.remove_employee("Michael Black")

        sanrio.show_info()
        sanrio2 = SanrioCompany(123)
        print(sanrio._specialization)
    except Exception as error:
        print(error)
