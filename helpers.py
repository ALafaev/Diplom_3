import random

def user_registration_data():
    user_email = f'anton_lafaev_15_{random.randint(1000,9999)}@yandex.ru'
    user_password = 'qwerty'
    user_name = 'Антон'
    return {
        "email": user_email,
        "password": user_password,
        "name": user_name
    }
