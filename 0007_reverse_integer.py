def reverse(x):
    negative = True if x < 0 else False
    x_str = str(x)[::-1].replace('-', '')

    if int(x_str) > 2**31:
        return 0

    if negative:
        return int(x_str) * -1

    return int(x_str)


def reverse2(x):
    is_negative = True if x < 0 else False

    if is_negative:
        x *= -1

    x_str = str(x)[::-1]
    x_int = int(x_str)

    if x_int > 2 ** 31:
        return 0
    elif is_negative:
        return x_int*-1
    else:
        return x_int





print(reverse2(9646324351))
