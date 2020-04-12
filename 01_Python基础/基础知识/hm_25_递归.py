def sum_num(num):
    """
    递归算法计算前n项之和
    :param num: 指定的前n项
    :return: int
    """
    assert isinstance(num, int)
    if num > 0:
        return num + sum_num(num - 1)
    else:
        return 0


sum1 = sum_num(100)
print(sum1)
