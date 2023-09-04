# 2 - У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] ,
# перетворити його у список змінних для Пайтона space_case, "friends_list", "my_tuple"]

camel_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_list = []

for var in camel_list:
    snake_name = []
    for let in var:
        if let.isupper():
            snake_name.extend(["_", let.lower()])
        else:
            snake_name.append(let)
    if snake_name[0] == "_":
        snake_name.pop(0)
    snake_list.append("".join(snake_name))

print(snake_list)
