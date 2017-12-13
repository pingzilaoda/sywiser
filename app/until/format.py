# !/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
from sqlalchemy.engine import ResultProxy

def format_date(value, format_='%Y-%m-%d'):
    """
    将日期格式化成字符串
    :param value: 将要格式化的date或者datetime对象
    :param format_: 格式化字符串，默认为'%Y-%m-%d'，也可以为'%Y-%m-%d %H:%M:%S'等
    """
    return value.strftime(format_)


def str_now():
    """
    获取当前时间字符串表示
    """
    return format_date(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")


def _format_item_value(value):
    """
    sxw 2016-8-17

    针对查询出来的模型列表字段值，可能不是符合要求的，进行格式化

    :param value: 待解析字段值
    :return list: 解析完之后的值
    """
    # 针对大多数情况，是字符串等类型，放第一位
    if isinstance(value, (unicode, str, int, float, long)):
        pass
    elif isinstance(value, datetime.datetime):
        value = format_date(value, format_='%Y-%m-%d %H:%M:%S')
    elif isinstance(value, datetime.date):
        value = format_date(value)
    elif isinstance(value, set):
        value = list(value)
    return value


def format_result(result_proxy):
    """
    sxw 2016-8-17

    格式化数据库查出来的结果进行字典化和列表化

    :param result_proxy: 数据库查询出来的结果集
    :return list: 结果集列表，可能为空
    """
    results = None
    if isinstance(result_proxy, ResultProxy):
        if result_proxy.rowcount:
            results = []
            for row in result_proxy:
                results.append({k: _format_item_value(v) for k, v in row.items()})
    return results