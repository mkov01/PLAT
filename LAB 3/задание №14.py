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
                print(f"✅ Пароль для пользователя {self.user} успешно изменен.")
            else:
                print("❌ Ошибка: Новый пароль слишком короткий (минимум 6 символов)!")
        else:
            print(f"❌ Ошибка: Неверный старый пароль для {self.user}!")

    def show_security_status(self):
        """Метод 3: Отображение статуса безопасности (без вывода самого пароля)"""
        masked_pwd = "*" * len(self._password)
        print(f"🔒 Пользователь: {self.user} | Длина пароля: {len(self._password)} симв. [{masked_pwd}]")

# Тест-сценарий
p1 = Password("admin", "root123")
p2 = Password("user_olga", "qwerty")
p3 = Password("dev_team", "pass2026")

p1.show_security_status()
p2.change_password("wrong_old", "new_pass")  # Неверный старый
p3.change_password("pass2026", "secret_key")  # Успешно
p3.show_security_status()