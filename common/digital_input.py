def digital_input(text):
    result = None
    while result is None:
        result = input(text)
        if result.isdigit():
            result = int(result)
            break

        print("Wrong enter")
        result = None

    return result
