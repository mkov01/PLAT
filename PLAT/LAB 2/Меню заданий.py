# =====================================================================
# ЛАБОРАТОРНАЯ РАБОТА №2. ИНТЕРАКТИВНОЕ МЕНЮ ЗАДАНИЙ (1, 8, 16)
# =====================================================================

while True:
    print("=== ГЛАВНОЕ МЕНЮ ===")
    print("1  - Задание №1 (Сумма, разность, произведение, частное)")
    print("8  - Задание №8 (Форматирование секунд в чч:мм:сс)")
    print("16 - Задание №16 (Площадь треугольника по формуле Герона)")
    print("0  - Выход из программы")
    print("====================")

    choice = int(input("Выберите номер задания для запуска: "))
    print("\n" + "="*40 + "\n")

    if choice == 1:
        print("--- ЗАДАНИЕ №1 (Базовый уровень) ---")
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        sum_res = num1 + num2
        diff_res = num1 - num2
        prod_res = num1 * num2
        quot_res = num1 / num2

        print("Сумма:", sum_res)
        print("Разность:", diff_res)
        print("Произведение:", prod_res)
        print("Частное:", quot_res)

    elif choice == 8:
        print("--- ЗАДАНИЕ №8 (Средний уровень) ---")
        total_seconds = int(input("Введите количество секунд: "))

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        print("Время в формате часы:минуты:секунды:")
        print(hours, minutes, seconds, sep=":")

    elif choice == 16:
        print("--- ЗАДАНИЕ №16 (Повышенный уровень) ---")
        side_a = float(input("Введите сторону a: "))
        side_b = float(input("Введите сторону b: "))
        side_c = float(input("Введите сторону c: "))

        perimeter = side_a + side_b + side_c
        half_perimeter = perimeter / 2
        area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c)) ** 0.5

        print("Периметр:", perimeter)
        print("Полупериметр:", half_perimeter)
        print("Площадь по формуле Герона:", area)

    elif choice == 0:
        print("Выход из программы. До свидания!")
        print("\n" + "="*40 + "\n")
        break  # Выходим из бесконечного цикла

    else:
        print("Ошибка! Задания с таким номером нет в меню.")

    print("\n" + "="*40 + "\n")
