from common.input_an_integer import digital_input_2


def positive_digital_input(text):
    result = None
    while result is None:
        result = digital_input_2(text)
        if result > 0:
            break
        print('Wrong enter, a natural number expected')
        result = None

    return result
