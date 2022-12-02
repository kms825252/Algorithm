def split_and_sum(text):
    if text == "":
        return 0

    return get_sum(get_int_lst(text.split('-')))


def get_sum(ing_lst):
    result = 0
    for val in ing_lst:
        result += int(val)
    return result


def get_int_lst(values):
    ing_lst = []
    for val in values:
        ing_lst.append(int(val))
    return ing_lst


ret = split_and_sum("11-22-33")
print(ret)