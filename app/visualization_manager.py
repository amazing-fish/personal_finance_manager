import matplotlib.pyplot as plt
from record_manager import get_income_records, get_expense_records
from collections import defaultdict


def plot_income_expense_pie_chart():
    income_records = get_income_records()
    expense_records = get_expense_records()

    income_total = sum([record['amount'] for record in income_records])
    expense_total = sum([record['amount'] for record in expense_records])

    labels = ['Income', 'Expense']
    sizes = [income_total, expense_total]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title('Income vs Expense')
    plt.show()


def plot_category_pie_chart(record_type: str):
    if record_type == 'income':
        records = get_income_records()
    else:
        records = get_expense_records()

    category_amounts = defaultdict(float)

    for record in records:
        category_amounts[record['category']] += record['amount']

    labels = list(category_amounts.keys())
    sizes = [amount for amount in category_amounts.values()]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title(f'{record_type.capitalize()} by Category')
    plt.show()

# 添加其他可视化相关的函数
