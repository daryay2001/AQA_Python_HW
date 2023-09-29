# Опишіть класи, використовуючи принципи з уроку. Ви повинні реалізувати різні атрибути
# (мінімум 2 для батьківського класу) і методи (мінімум 2 для кожного з класів)
#
# For example:
#
# Animals -> mammals -> flying mammals-> Bird -> Eagle
#
# ............................
#
# Слід запровадити щонайменше 3 ланцюжки наслідування
#
# Класи мають бути в різних модулях. У вас повинно бути не менше 9 різних класів.

from yacht import Yacht
from tanker_vessel import Tanker
from reefer_vessel import Reefer
from container_vessel import ContainerVessel
from liner_vessel import Liner


def show_info(vessel):
    return vessel.vessel_info()  # polymorphism


def make_money(vessel):
    return vessel.trade()  # polymorphism


if __name__ == '__main__':
    try:
        bystritsa = Yacht("Bystritsa", 2019, 1234567, 5, 20.5,
                          "steel and wood", "G", 10)
        bystritsa.vessel_info()
        print(bystritsa.get_imo("1234"))
        print("________________________________")
        bystritsa.trade()
        bystritsa.be_winner()
        print(bystritsa.crew_attr)
        print(bystritsa.entert_attr)
        print("________________________________")

        star = Tanker("Green Star", 2001, 4545454, 17.8, 15.6, "steel",
                      "Middle East", "Oil", 50000)

        star.vessel_info()
        star.transport_liquid()
        print(star.get_imo("1234"))
        print(star.get_imo(1234633))
        star.trade()
        print(star.tanker_attr)
        print(star.liquid_attr)
        print("________________________________")

        my_star = Reefer("Cold Star", 2001, 4545454, 17.8, 15.6, "steel",
                         "Middle East", "Fish", 12500)
        my_star.vessel_info()
        print(my_star.get_imo("1234"))
        my_star.keep_safe()
        print(my_star.reefer_attr)
        print(my_star.temperature)
        print("________________________________")

        ever = ContainerVessel(name="Ever Golden", year=2015, imo=5555555, draft=20.8, speed=22.5,
                               material="steel", direction="Far East - Middle East", container_capacity=12450)
        ever.vessel_info()
        print(ever.get_imo("1234"))
        ever.trade()
        print(ever.teu)
        print(ever.cont_holds)
        print("________________________________")

        queen = Liner("Queen Elizabeth", 1940, 3456789, 12,
                      28, "wood and steel", 2283, "Northern Europe")
        queen.vessel_info()
        print(queen.get_imo("1234"))
        queen.trade()
        queen.be_on_cruise()
        print(queen.ticket_attr)
        print(queen.liner_attr)
        print("________________________________")

        show_info(ever)  # polymorphism
        print("________________________________")
        show_info(bystritsa)  # polymorphism
        print("________________________________")

        make_money(queen)  # polymorphism
        print("________________________________")
        make_money(star)  # polymorphism

    except Exception as error:
        print(error)
