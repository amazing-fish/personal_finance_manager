import sqlite3
import csv
import os
from typing import List, Tuple, Dict
from contextlib import closing

DB_PATH = r'E:\Project\GitHub\personal_finance_manager\data/database.sqlite'
CATEGORIES_CSV_PATH = r'E:\Project\GitHub\personal_finance_manager\data/categories.csv'


def create_database():
    with closing(sqlite3.connect(DB_PATH)) as connection:
        cursor = connection.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            note TEXT
        )
        """)

        connection.commit()


def import_categories() -> List[str]:
    if not os.path.exists(CATEGORIES_CSV_PATH):
        return []

    categories = []
    with open(CATEGORIES_CSV_PATH, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            categories.append(row[0])

    return categories


def add_record(record: Tuple[str, str, float, str, str]):
    with closing(sqlite3.connect(DB_PATH)) as connection:
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO records (type, category, amount, date, note)
        VALUES (?, ?, ?, ?, ?)
        """, record)
        connection.commit()


def get_records() -> List[Dict[str, str]]:
    with closing(sqlite3.connect(DB_PATH)) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM records")
        rows = cursor.fetchall()

    records = [
        {
            'id': row[0],
            'type': row[1],
            'category': row[2],
            'amount': row[3],
            'date': row[4],
            'note': row[5]
        }
        for row in rows
    ]

    return records

# 添加其他数据管理相关的函数
