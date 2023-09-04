# 2. Користувач вводить текст і слово, яке потрібно знайти,
# якщо це слово є в тексті, вивести 'YES', інакше 'NO'

# ver1
# Будемо вважати, що регист слова не має значення, отже, шукаємо слово за змістом.

user_text = input("Enter your text: ").lower()
word_to_find = input("Enter word to find: ").lower().strip()

print("YES") if word_to_find in user_text else print("NO")

# ver2

user_text = input("Enter your text: ").lower()
word_to_find = input("Enter word to find: ").lower().strip()

if user_text.find(word_to_find) != -1:
    print("YES")
else:
    print("NO")

# Якщо слова немає, поверне -1, можна також замість find можна використати count:
# if user_text.count(word_to_find) != 0
