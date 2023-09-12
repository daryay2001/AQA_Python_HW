# # 1 - Відкрити файл test_file.csv, прочитати його, зп співробітників
# # у доларах перевести в гривні на поточну дату (курс задається окремою змінною).
# # Результат зберегти новий файл salaries_uah.csv
#
import csv
import os

grn_rate = 36.95

usd_salary = "test_file.csv"

try:
    with open(usd_salary, "r") as file:
        lines = file.readlines()

    # Розділимо дані на рядки через кому
    rows = [line.strip().split(",") for line in lines]

    header = rows[0] # Оскільки перший ряд - заголовок із назвами
    salary = rows[1:]

    for i in range(len(salary)):
        for j in range(1, len(salary[i])): # оскільки в першій клітинці ім`я
            salary[i][j] = str(float(salary[i][j]) * grn_rate)

    grn_salary = "salaries_uah.csv"

    with open(grn_salary, "w") as file:
        file.write(",".join(header) + "\n") # Знову записали заголовок

        for row in salary:
            file.write(",".join(row) + "\n")

    print("Your salary is converted to grn")


except Exception as error:
    print(error)


