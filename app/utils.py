import datetime


def format_date(date: datetime.date) -> str:
    """
    将日期对象格式化为字符串
    :param date: 日期对象
    :return: 格式化后的字符串
    """
    return date.strftime('%Y-%m-%d')


def parse_date(date_str: str) -> datetime.date:
    """
    将字符串解析为日期对象
    :param date_str: 日期字符串
    :return: 解析后的日期对象
    """
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()


def format_currency(amount: float) -> str:
    """
    将金额格式化为货币字符串
    :param amount: 金额
    :return: 格式化后的货币字符串
    """
    return f'{amount:,.2f}'


def is_valid_number(input_str: str) -> bool:
    """
    检查输入字符串是否为有效数字（整数或小数）
    :param input_str: 输入字符串
    :return: 如果输入字符串为有效数字则返回 True，否则返回 False
    """
    try:
        float(input_str)
        return True
    except ValueError:
        return False

# 根据需求添加其他通用工具函数
