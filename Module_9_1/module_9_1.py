def apply_all_func(int_list, *functions):
    res_dict = {}
    for func in functions:
        res_dict[func.__name__] = func(int_list)
    return res_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))


# Моя попытка сортировки:
def __str_to_numeric_str(string):
    st = string
    for n in range(len(string)):
        if string[n].isalpha():
            st = st.replace(string[n], '')
    return float(st)


def __convert_int_list(any_list):
    returned_list = []
    for i in any_list:
        if isinstance(i, int) and not isinstance(i, bool):
            returned_list.append(i)
            continue
        if isinstance(i, float):
            returned_list.append(int(i))
            continue
        if isinstance(i, str):
            if i.isnumeric():
                i = int(i)
                returned_list.append(i)
                continue
            if i.isalpha():
                returned_list.append(0)
                continue
            else:
                numeric_str = __str_to_numeric_str(i)
                res = int(numeric_str)
                returned_list.append(res)
                continue
        if isinstance(i, bytes):
            i_decoded = i.decode()
            if i_decoded.isnumeric():
                returned_list.append(int(i_decoded))
            else:
                returned_list.append(0)
        if isinstance(i, bool):
            if i:
                returned_list.append(1)
            else:
                returned_list.append(0)
    return returned_list


def apply_all_func_1(int_list, *functions):
    res_dict = {}
    filtered_list = __convert_int_list(int_list)
    for func in functions:
        res_dict[func.__name__] = func(filtered_list)
    return res_dict


print(apply_all_func_1([6, 20, 15, 9], max, min))
print(apply_all_func_1([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func_1([6, 20, 15, 9, b'\x33', 'abx123', '22', 'gx', 45.27, 'str21135.55',
                        '222.562312asd', True], len, sum, sorted, max, min))
