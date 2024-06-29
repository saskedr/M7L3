import random
import string

def generate_password(length=12):
    """Генерация случайного пароля заданной длины (не менее 8 символов)."""
    if length < 8:
        print("Минимальная длина пароля должна быть 8 символов. Пароль будет установлен длиной 8 символов.")
        length = 8
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Пример использования
password_length = int(input("Введите длину пароля (не менее 8): "))
print("Ваш новый пароль:", generate_password(password_length))