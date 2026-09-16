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


# ==========================================
# ЗАДАНИЕ №3: КЛАСС STUDENT
# ==========================================
class Student:
    def __init__(self, name: str, age: int, specialty: str):
        self.name = name
        self.age = age
        self.specialty = specialty

    def display_info(self):
        """Метод 1: Вывод информации о студенте"""
        print(f" Студент: {self.name} | Возраст: {self.age} | Специальность: {self.specialty}")

    def change_specialty(self, new_specialty: str):
        """Метод 2: Изменение специальности"""
        print(f" --> {self.name} переведен на специальность: {new_specialty}")
        self.specialty = new_specialty

    def celebrate_birthday(self):
        """Метод 3: Увеличение возраста (день рождения)"""
        self.age += 1
        print(f" 🎉 У {self.name} день рождения! Теперь ему/ей {self.age} лет.")


def task_3():
    clear_screen()
    print_header("ЗАДАНИЕ №3: УПРАВЛЕНИЕ СТУДЕНТАМИ")
    print(" 🛠 Создаем тестовых студентов и запускаем сценарий:\n")
    
    s1 = Student("Адиль", 19, "ВТПО")
    s2 = Student("Алина", 20, "Маркетинг")
    s3 = Student("Руслан", 18, "Data Science")

    print("-" * 55)
    s1.display_info()
    s2.display_info()
    s3.display_info()
    print("-" * 55)
    
    print("\n [Действие 1] Студент Адиль меняет специальность:")
    s1.change_specialty("Архитектура")
    
    print("\n [Действие 2] У Руслана день рождения:")
    s3.celebrate_birthday()
    
    print("\n" + "-" * 55)
    print(" ✔ Итоговое состояние студентов:")
    s1.display_info()
    s3.display_info()
    print("-" * 55)


# ==========================================
# ЗАДАНИЕ №14: КЛАСС PASSWORD
# ==========================================
class Password:
    def __init__(self, user: str, initial_password: str):
        self.user = user
        self._password = initial_password  # Закрытый атрибут

    def check_password(self, password_to_test: str) -> bool:
        """Метод 1: Проверка совпадения пароля"""
        return self._password == password_to_test

    def change_password(self, old_password: str, new_password: str):
        """Метод 2: Изменение пароля с проверкой старого"""
        if self.check_password(old_password):
            if len(new_password) >= 6:  # Простейшая валидация длины
                self._password = new_password
                print(f" ✅ Пароль для пользователя {self.user} успешно изменен.")
            else:
                print(" ❌ Ошибка: Новый пароль слишком короткий (минимум 6 символов)!")
        else:
            print(f" ❌ Ошибка: Неверный старый пароль для {self.user}!")

    def show_security_status(self):
        """Метод 3: Отображение статуса безопасности (без вывода самого пароля)"""
        masked_pwd = "*" * len(self._password)
        print(f" 🔒 Пользователь: {self.user} | Длина пароля: {len(self._password)} симв. [{masked_pwd}]")


def task_14():
    clear_screen()
    print_header("ЗАДАНИЕ №14: МЕНЕДЖЕР ПАРОЛЕЙ")
    print(" 🛠 Создаем учетные записи и проверяем безопасность:\n")
    
    p1 = Password("admin", "root123")
    p2 = Password("user_olga", "qwerty")
    p3 = Password("dev_team", "pass2026")

    print("-" * 55)
    p1.show_security_status()
    p2.show_security_status()
    p3.show_security_status()
    print("-" * 55)

    print("\n [Попытка 1] Ольга пробует сменить пароль, указав неверный старый:")
    p2.change_password("wrong_old", "new_pass")  # Неверный старый

    print("\n [Попытка 2] Команда разработчиков меняет пароль на надежный:")
    p3.change_password("pass2026", "secret_key")  # Успешно
    
    print("\n" + "-" * 55)
    print(" ✔ Финальный статус безопасности:")
    p3.show_security_status()
    print("-" * 55)


# ==========================================
# ЗАДАНИЕ №18: КЛАССЫ GROUPSTUDENT И GROUP
# ==========================================
class GroupStudent:
    """Вспомогательный класс студента для хранения личных данных"""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Group:
    """Основной класс для управления списком студентов"""
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.__students = []  # Скрытый список студентов внутри группы

    def add_student(self, student: GroupStudent):
        """Метод 1: Добавление студента в группу"""
        self.__students.append(student)
        print(f" ➕ Студент {student.name} добавлен в группу {self.group_name}")

    def remove_student(self, student_name: str):
        """Метод 2: Удаление студента по имени"""
        for student in self.__students:
            if student.name == student_name:
                self.__students.remove(student)
                print(f" ➖ Студент {student_name} удален из группы {self.group_name}")
                return
        print(f" ❓ Студент {student_name} не найден в группе {self.group_name}")

    def get_average_age(self) -> float:
        """Метод 3: Подсчет среднего возраста студентов в группе"""
        if not self.__students:
            return 0.0
        total_age = sum(student.age for student in self.__students)
        return round(total_age / len(self.__students), 1)

    def display_group(self):
        """Метод 4: Вывод всего состава группы"""
        print(f"\n 👥 Состав группы {self.group_name} (Средний возраст: {self.get_average_age()}):")
        if not self.__students:
            print("    Группа пуста.")
        for student in self.__students:
            print(f"    - {student.name}, {student.age} лет")


def task_18():
    clear_screen()
    print_header("ЗАДАНИЕ №18: УПРАВЛЕНИЕ УЧЕБНЫМИ ГРУППАМИ")
    print(" 🛠 Создаем группу ИС-24, студентов и выполняем операции:\n")
    
    group_it = Group("ИС-24")

    # Создаем студентов
    st1 = GroupStudent("Медет", 19)
    st2 = GroupStudent("Айша", 21)
    st3 = GroupStudent("Кирилл", 20)

    print("-" * 55)
    group_it.add_student(st1)
    group_it.add_student(st2)
    group_it.add_student(st3)
    print("-" * 55)

    group_it.display_group()

    print("\n [Действие] Удаляем студента Айшу из группы:")
    group_it.remove_student("Айша")
    
    print("-" * 55)
    group_it.display_group()
    print("-" * 55)


# ==========================================
# ГЛАВНОЕ МЕНЮ ПРОГРАММЫ
# ==========================================
def main_menu():
    while True:
        clear_screen()
        print("=" * 55)
        print("║" + " ГЛАВНОЕ МЕНЮ ОБЪЕКТНО-ОРИЕНТИРОВАННЫХ ЗАДАЧ ".center(53, " ") + "║")
        print("=" * 55)
        print("  [1] Задание №3  (Класс Student)")
        print("  [2] Задание №14 (Класс Password / Инкапсуляция)")
        print("  [3] Задание №18 (Классы Group и GroupStudent)")
        print("  [0] Выход из программы")
        print("=" * 55)
        
        choice = input("  ► Выберите номер пункта меню: ").strip()
        
        if choice == '1':
            task_3()
        elif choice == '2':
            task_14()
        elif choice == '3':
            task_18()
        elif choice == '0':
            clear_screen()
            print("\n  Программа успешно завершена. Всего доброго!\n")
            sys.exit()
        else:
            print("\n  [!] Неверный пункт. Нажмите Enter, чтобы попробовать снова...")
            
        input("\n  Нажмите Enter для возврата в меню...")

if __name__ == "__main__":
    main_menu()