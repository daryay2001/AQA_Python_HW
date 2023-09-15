# 3 - Напишіть функцію з такою сигнатурою: def display_box(width: int, height: int, character="*") .
# Ця функція намалює простий прямокутник заданої висоти та ширини,
# використовуючи character для друку ліній. Наприклад, display_box(5, 4, 'x') має вивести наступне:
#
# xxxxx
#
# x x
#
# x x
#
# xxxxx

def display_box(width: int, height: int, character="*"):
    if not isinstance(width, int) or not isinstance(height, int):
        print("Incorrect value of the length")
    else:
        for i in range(height):
            if i == 0 or i == height-1:
                print(character * width)
            else:
                space = " " * (width - 4) # Саме мінус 4 для гарного вигляду у консолі
                print(f"{character} {space} {character}")


if __name__ == "__main__":
    try:
        display_box(5, 4, "x")
        display_box(4, 5, "x")
        display_box(width=7, height=2, character="x")
        display_box(7.5, 2.6)
        display_box(6.3, 7)

    except Exception as error:
        print(error)
