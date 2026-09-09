side_a = float(input("Введите длину стороны a: "))
side_b = float(input("Введите длину стороны b: "))
side_c = float(input("Введите длину стороны c: "))

perimeter = side_a + side_b + side_c
half_perimeter = perimeter / 2

area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c)) ** 0.5

print("Периметр треугольника:", perimeter)
print("Полупериметр треугольника:", half_perimeter)
print("Площадь треугольника:", area)