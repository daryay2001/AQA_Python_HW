# Існує список з іменами ["john", "marta", "james", "amanda", "marianna"],
# перетворити рядок, щоб кожне ім'я явно починалися з великої літери.

names_list = ["john", "marta", "james", "amanda", "marianna"]
capital_names = [name.capitalize() for name in names_list]

print(capital_names)