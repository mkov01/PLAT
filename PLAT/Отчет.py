import os
import sys

def clear_screen():
    """Очистка консоли для красивого переключения между задачами"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Красивая рамка для заголовков"""
    print("\n" + "=" * 55)
    print(f"║ {title.center(51)} ║")
    print("=" * 55)

def task_2():
    clear_screen()
    print_header("ЗАДАНИЕ №2: РАСЧЕТ ПРЯМОУГОЛЬНИКА")
    try:
        a = float(input("  ► Введите длину прямоугольника: "))
        b = float(input("  ► Введите ширину прямоугольника: "))
        
        if a <= 0 or b <= 0:
            print("\n  [!] Ошибка: Стороны должны быть строго больше нуля!")
            return
            
        S = a * b
        P = 2 * (a + b)
        
        print("\n" + "-" * 55)
        print(f"  ✔ Результаты вычислений:")
        print(f"    • Площадь (S) : {S:,.2f}")
        print(f"    • Периметр (P): {P:,.2f}")
        print("-" * 55)
        
    except ValueError:
        print("\n  [!] Ошибка: Пожалуйста, вводите только числа. Для дробей — точка.")

def task_10():
    clear_screen()
    print_header("ЗАДАНИЕ №10: ПОРАЗРЯДНЫЙ РАЗБОР ЧИСЛА")
    try:
        num = int(input("  ► Введите четырехзначное целое число: "))
        
        if not (1000 <= abs(num) <= 9999):
            print("\n  [!] Ошибка: Число должно содержать ровно 4 цифры!")
            return
            
        num = abs(num)
        thousands = num // 1000
        hundreds = (num % 1000) // 100
        tens = (num % 100) // 10
        units = num % 10
        
        print("\n" + "-" * 55)
        print("  ✔ Выделенные разряды:")
        print(f"    • Тысячи : {thousands}")
        print(f"    • Сотни   : {hundreds}")
        print(f"    • Десятки : {tens}")
        print(f"    • Единицы : {units}")
        print("-" * 55)
        
    except ValueError:
        print("\n  [!] Ошибка: Введено не целое число!")

def task_17():
    clear_screen()
    print_header("ЗАДАНИЕ №17: КАПИТАЛИЗАЦИЯ ВКЛАДА")
    try:
        principal = float(input("  ► Введите начальную сумму вклада: "))
        rate = float(input("  ► Введите годовую ставку (%): "))
        years = int(input("  ► Введите срок вклада (лет): "))
        
        if principal < 0 or rate < 0 or years < 0:
            print("\n  [!] Ошибка: Параметры не могут быть отрицательными.")
            return
            
        amount = principal * ((1 + rate / 100) ** years)
        profit = amount - principal
        
        print("\n" + "-" * 55)
        print("  ✔ Финансовый отчет:")
        print(f"    • Итоговая сумма на счете: {amount:,.2f}")
        print(f"    • Чистая прибыль         : {profit:,.2f}")
        print("-" * 55)
        
    except ValueError:
        print("\n  [!] Ошибка: Неверный формат данных.")

def main_menu():
    while True:
        clear_screen()
        print("=" * 55)
        print("║" + " ГЛАВНОЕ МЕНЮ ЛАБОРАТОРНОЙ РАБОТЫ ".center(53, " ") + "║")
        print("=" * 55)
        print("  [1] Задание №2  (Площадь и периметр прямоугольника)")
        print("  [2] Задание №10 (Разбор четырехзначного числа)")
        print("  [3] Задание №17 (Ежегодная капитализация вклада)")
        print("  [0] Выход из программы")
        print("=" * 55)
        
        choice = input("  ► Выберите номер пункта меню: ").strip()
        
        if choice == '1':
            task_2()
        elif choice == '2':
            task_10()
        elif choice == '3':
            task_17()
        elif choice == '0':
            clear_screen()
            print("\n  Программа успешно завершена. Всего доброго!\n")
            sys.exit()
        else:
            print("\n  [!] Неверный пункт. Нажмите Enter, чтобы попробовать снова...")
            
        input("\n  Нажмите Enter для возврата в меню...")

if __name__ == "__main__":
    main_menu()
