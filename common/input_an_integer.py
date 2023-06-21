import re


def digital_input_2(text):
    regex = r'[-]?\d+'
    result = None
    while result is None:
        result = input(text)
        if re.fullmatch(regex, result):
            result = int(result)
            break

        print('Wrong enter, a number expected')
        result = None

    return result
