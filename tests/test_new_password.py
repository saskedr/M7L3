import string
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters
def test_error():
    password = generate_password('s')
    assert password == "Введите число"
def test_passw():
    password = generate_password(10)
    assert password == password
def test_otric():
    password = generate_password(-10)
    assert password == ""
def test_generate_password_generates_unique_passwords():
    passwords = [generate_password(10) for _ in range(100)]
    assert len(set(passwords)) == len(passwords)
def test_generate_password_with_valid_length():
    password = generate_password(10)
    assert len(password) == 10
    assert isinstance(password, str)


"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""