from datetime import datetime
from copy import deepcopy


def deep_merge_dict(x, y):
    """
    深合并字典
    :param x:
    :param y:
    :return:
    """
    z = deepcopy(x)
    z.update(y)
    for k, v in z.items():
        if k in x and k in y:
            if isinstance(x[k], dict) and isinstance(y[k], dict):
                z[k] = deep_merge_dict(x[k], y[k])
    return z


def hundred_ns_to_string(hundred_ns: int) -> str:
    """
    百纳秒转可读字符串 HH:mm:ss
    :return:
    """
    sec = hundred_ns // 10000000
    min = sec // 60
    hour = min // 60
    return str(hour).zfill(2) + ":" + str(min % 60).zfill(2) + ":" + str(sec % 60).zfill(2)


def byte_to_string(byte: int) -> str:
    """
    字节转可读字符串
    :return:
    """
    if byte < 1024:
        return str(byte) + " B"
    elif byte < 1024 * 1024:
        return str(round(byte / 1024, 2)) + " KB"
    elif byte < 1024 * 1024 * 1024:
        return str(round(byte / 1024 / 1024, 2)) + " MB"
    else:
        return str(round(byte / 1024 / 1024 / 1024, 2)) + " GB"