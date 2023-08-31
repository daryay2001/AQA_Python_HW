# 4. Користувач вводить текст через пробіл. Конвертувати текст у список.
# Вивести останні 3 елементи зі списку, якщо список містить менше 3-х елементів,
# вивести повідомлення про те що кількість елементів менша за 3
# і вказати кількість елементів поточного списку.

# ver1

user_text = input("Enter your text: ")
words_list = user_text.split()

if len(words_list) >= 3:
    print(words_list[-3:])
else:
    print(f"There are less than 3 elements in list. There are {len(words_list)} elements.")


