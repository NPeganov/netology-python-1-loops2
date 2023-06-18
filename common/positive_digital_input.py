from common.digital_input import digital_input


def positive_digital_input(text):
    result = None
    while result is None:
        result = digital_input(text)
        if result <= 0:
            print("Wrong enter")
            result = None
        else:
            break

    return result
