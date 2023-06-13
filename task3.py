"""
Задание 3
Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам.
Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: ((revenue / cost) - 1) * 100

Пример работы программы:

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}
Результат:

{'adwords': {'revenue': 35, 'cost': 34, 'ROI': 2.94},
 'facebook': {'revenue': 103, 'cost': 110, 'ROI': -6.36},
 'twitter': {'revenue': 11, 'cost': 24, 'ROI': -54.17},
 'vk': {'revenue': 103, 'cost': 98, 'ROI': 5.1},
 'yandex': {'revenue': 179, 'cost': 153, 'ROI': 16.99}}

"""


ROI_INDEX = 'ROI'


def ROI_calc(revenue, cost):
    if cost == 0:
        # Тут нужен exception и запись в лог. Но мы это пока не проходили, поэтому просто возвращаем 0
        return 0

    return round(((revenue / cost) - 1) * 100, 2)


def ROI_add(to_add_roi):
    for val in to_add_roi.values():
        val[ROI_INDEX] = ROI_calc(val['revenue'], val['cost'])


def format_roi_output(to_add_roi):
    ROI_add(to_add_roi)  # добавили ROI к исходному словарю
    keys = sorted(to_add_roi.keys())
    last_key = keys[-1]
    formatted_roi = "{"
    for key in keys:
        output_str = f"'{key}': {to_add_roi.get(key)}"
        if key != last_key:
            formatted_roi += f"{output_str},\n "
        else:
            formatted_roi += f"{output_str}}}"

    return formatted_roi


if __name__ == '__main__':
    results = {
        'vk': {'revenue': 103, 'cost': 98},
        'yandex': {'revenue': 179, 'cost': 153},
        'facebook': {'revenue': 103, 'cost': 110},
        'adwords': {'revenue': 35, 'cost': 34},
        'twitter': {'revenue': 11, 'cost': 24},
    }

    print(format_roi_output(results))
