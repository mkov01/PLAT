try:
    principal = float(input("Введите сумму вклада: "))
    rate = float(input("Введите годовую ставку (%): "))
    years = int(input("Введите количество лет: "))

    amount = principal * ((1 + rate / 100) ** years)
    profit = amount - principal

    print(f"\nИтоговая сумма: {amount:.2f}")
    print(f"Чистый доход: {profit:.2f}")

except ValueError:
    print("Ошибка: вводите только числа. Для дробных значений используйте точку.")