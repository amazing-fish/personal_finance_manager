import csv
from typing import List
from data_manager import import_categories, DB_PATH
import sqlite3
from contextlib import closing

DB_PATH = 'data/database.sqlite'
CATEGORIES_CSV_PATH = 'data/categories.csv'


def get_categories() -> List[str]:
    return import_categories()


def add_category(category: str):
    categories = get_categories()
    if category not in categories:
        with open(CATEGORIES_CSV_PATH, 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([category])


def delete_category(category: str):
    categories = get_categories()
    if category in categories:
        categories.remove(category)

        with open(CATEGORIES_CSV_PATH, 'w') as csvfile:
            writer = csv.writer(csvfile)
            for cat in categories:
                writer.writerow([cat])

        with closing(sqlite3.connect(DB_PATH)) as connection:
            cursor = connection.cursor()
            cursor.execute("""
            DELETE FROM records
            WHERE category = ?
            """, (category,))
            connection.commit()

# 添加其他分类管理相关的函数
