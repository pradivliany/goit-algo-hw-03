import re


def normalize_phone(phone_number: str) -> str:
    """

    Функція нормалізує телефонний номер до потрібного формату

    :param phone_number: рядок з телефонним номером у різних форматах
    :return: нормалізований номер
    """
    my_pattern = '[^0-9]'
    clean_phone_num = re.sub(pattern=my_pattern, repl='', string=phone_number)
    print(clean_phone_num)
    if len(clean_phone_num) == 10:
        return '+38' + clean_phone_num
    elif len(clean_phone_num) == 12:
        return '+' + clean_phone_num
    else:
        raise ValueError('Невірний формат номера телефону')
