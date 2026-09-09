total_seconds = int(input("Введите количество секунд: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print("Результат в формате часы:минуты:секунды:")
print(hours, minutes, seconds, sep=":")