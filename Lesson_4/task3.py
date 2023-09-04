# 3 - Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників
# цих мов (значення). Виведіть по черзі для усіх елементів словника повідомлення
# типу My favorite programming language is Python. It was created by Guido van Rossum..
# Видаліть, на ваш вибір, одну пару «мова: розробник» із словника. Виведіть словник на екран.

leng_dict = {"Python": "Guido van Rossum",
             "JS": "Brendan Eich",
             "C++": "Bjarne Stroustrup",
             "Java": "James Gosling"}

for key, value in leng_dict.items():
    print(f"My favorite programming language is {key}. It was created by {value}.")

del leng_dict["C++"]
print(leng_dict)