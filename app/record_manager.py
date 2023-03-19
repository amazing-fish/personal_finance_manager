from typing import Tuple
from data_manager import add_record, get_records


def add_income(category: str, amount: float, date: str, note: str = None):
    record = ('income', category, amount, date, note)
    add_record(record)


def add_expense(category: str, amount: float, date: str, note: str = None):
    record = ('expense', category, amount, date, note)
    add_record(record)


def get_all_records():
    return get_records()


def get_income_records():
    all_records = get_records()
    income_records = [record for record in all_records if record['type'] == 'income']
    return income_records


def get_expense_records():
    all_records = get_records()
    expense_records = [record for record in all_records if record['type'] == 'expense']
    return expense_records

# 添加其他收入和支出记录管理相关的函数
