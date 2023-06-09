"""
Задание 4
Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж (пример структуры данных приведен
ниже). Напишите программу, которая возвращает название канала с максимальным объемом продаж.

Пример работы программы:

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

Результат: Максимальный объем продаж на рекламном канале: vk
"""


def max_amount_of_sales(sales_amount):
    # Мы твёрдо верим, что входные данные соответствуют нужной нам структуре, в противном случае программа упадёт
    return max(sales_amount, key=sales_amount.get)
    # Тут можно прочитать о выше-использованной конструкции
    # https://teletype.in/@pythontalk/key_with_max_value


if __name__ == '__main__':
    stats = {'facebook': 50, 'yandex': 18, 'vk': 140, 'google': 64, 'email': 27, 'ok': 58}
    print(f"Maximum sales volume on the advertising channel: {max_amount_of_sales(stats)}")
