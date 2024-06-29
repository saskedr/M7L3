import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters
def validate_len(len1=12):
    password = generate_password(len1)
    assert len1 == len(password)
"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""

def test_password_length():
    password_length = 12 
    password = ''
    password = generate_password()
    assert len(password) == password_length

def test_password_difference():
    password_1 = ''
    password_1 = generate_password()
    password_2 = ''
    password_2 = generate_password()
    assert password_1 != password_2