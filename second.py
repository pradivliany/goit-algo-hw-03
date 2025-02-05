from random import sample


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Функція допомагає генерувати набір унікальних випадкових чисел

    :param min: мінімальне можливе число в наборі (не менше 1)
    :param max: максимальне можливе число в наборі (не більше 1000)
    :param quantity: кількість чисел, які потрібно вибрати (між min і max)
    :return: список випадково вибраних, відсортованих чисел
    """

    try:
        nums = list(range(min, max + 1))
        return sorted(sample(nums, quantity))
    except (ValueError, TypeError):
        return []
