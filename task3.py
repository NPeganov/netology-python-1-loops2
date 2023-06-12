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


def ROI_calc(revenue, cost):
    return round(((revenue / cost) - 1) * 100, 2)


def ROI_add(results):
    for val in results.values():
        val['ROI'] = ROI_calc(val['revenue'], val['cost'])

    return results


def output(results):
    roi_added = ROI_add(results)
    keys = sorted(roi_added.keys())
    last_key = keys[-1]
    first_key = keys[0]
    for key in keys:
        output_str = f"'{key}': {roi_added.get(key)}"
        if key == first_key:
            print(f"{{{output_str},")
        elif key != last_key:
            print(f"{output_str},")
        else:
            print(f"{output_str}}}")
        # Здесь вывод будет в том же порядке, что и была дана переменная. В примере же вывод был в другом порядке


if __name__ == '__main__':
    results = {
        'vk': {'revenue': 103, 'cost': 98},
        'yandex': {'revenue': 179, 'cost': 153},
        'facebook': {'revenue': 103, 'cost': 110},
        'adwords': {'revenue': 35, 'cost': 34},
        'twitter': {'revenue': 11, 'cost': 24},
    }

    output(results)
