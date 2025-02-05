import datetime


def get_days_from_today(date: str) -> int:
    """
    Функція розраховує кількість днів між заданою датою і поточною датою

    :param date: рядок, що представляє дату у форматі 'РРРР-ММ-ДД'
    :return: ціле число, як кількість днів між заданою датою і поточною
    """
    try:
        _format = '%Y-%m-%d'
        input_date_ordinal = datetime.datetime.strptime(date, _format).toordinal()
        today_date_ordinal = datetime.datetime.today().toordinal()
        return today_date_ordinal - input_date_ordinal

    except ValueError as err:
        print(f"Виникла помилка: {err}.\nВкажіть коректні дані у форматі 'РРРР-ММ-ДД'")


