# 2 - Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата,
# і повертає 3 значення : периметр квадрата, площа квадрата та діагональ квадрата. Надрукуйте їх

def square(side):
    if side < 0:
        side = 0
        print("Was entered side value less than 0!")
    perimeter = side * 4
    area = side ** 2
    diagonal = round(side * (2 ** 0.5), 3)

    return perimeter, area, diagonal


if __name__ == "__main__":
    try:
        for i in range(-5, 7, 5): # від -5 до 7 із кроком 5
            my_perim, my_area, my_diag = square(i)
            print(f"Perimeter of the square: {my_perim} cm")
            print(f"Area of the square: {my_area} cm2")
            print(f"Diagonal of the square: {my_diag} cm")
            print("_________________")
        print(square("I am a string"))
    except ValueError as error:
        print("Invalid value")
    except Exception as error:
        print(error)
