from common.input_integer import input_integer


def positive_digital_input(text):
    result = None
    while result is None:
        result = input_integer(text)
        if result > 0:
            break
        print('Wrong enter, a natural number expected')
        result = None

    return result
