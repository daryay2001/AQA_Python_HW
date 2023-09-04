# 3. Написати валідатор для пошти. Користувач вводить пошту, а програма повинна перевірити,
# що в пошті є символ '@' і '.', і якщо це так, вивести "YES", інакше "NO"

# ver1
user_mail = input("Enter your email: ")

if "@" in user_mail and "." in user_mail:
    print("YES")
else:
    print("NO")

# ver2
user_mail = input("Enter your email: ")

if user_mail.find("@") != -1 and user_mail.find(".") != -1:
    print("YES")
else:
    print("NO")
