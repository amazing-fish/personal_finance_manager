import tkinter as tk
from tkinter import ttk
from tkinter import messagebox  # Add this line

from app import data_manager
from record_manager import add_income, add_expense
from category_manager import get_categories
from visualization_manager import plot_income_expense_pie_chart, plot_category_pie_chart


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Personal Finance Manager")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        self.create_add_record_tab()
        self.create_visualization_tab()

    def create_add_record_tab(self):
        add_record_frame = ttk.Frame(self.notebook)
        self.notebook.add(add_record_frame, text="Add Record")

        ttk.Label(add_record_frame, text="Type:").grid(row=0, column=0, sticky=tk.W, padx=20, pady=10)
        self.record_type = ttk.Combobox(add_record_frame, values=("income", "expense"), state="readonly")
        self.record_type.current(0)
        self.record_type.grid(row=0, column=1, sticky=tk.W)

        ttk.Label(add_record_frame, text="Category:").grid(row=1, column=0, sticky=tk.W, padx=20, pady=10)
        categories = get_categories()
        if categories:
            self.category = ttk.Combobox(add_record_frame, values=categories, state="readonly")
            self.category.current(0)
        else:
            self.category = ttk.Combobox(add_record_frame, values=categories)
        self.category.grid(row=1, column=1, sticky=tk.W)

        ttk.Label(add_record_frame, text="Amount:").grid(row=2, column=0, sticky=tk.W, padx=20, pady=10)
        self.amount = ttk.Entry(add_record_frame)
        self.amount.grid(row=2, column=1, sticky=tk.W)

        ttk.Label(add_record_frame, text="Date (YYYY-MM-DD):").grid(row=3, column=0, sticky=tk.W, padx=20, pady=10)
        self.date = ttk.Entry(add_record_frame)
        self.date.grid(row=3, column=1, sticky=tk.W)

        ttk.Label(add_record_frame, text="Note:").grid(row=4, column=0, sticky=tk.W, padx=20, pady=10)
        self.note = ttk.Entry(add_record_frame)
        self.note.grid(row=4, column=1, sticky=tk.W)

        self.submit_button = ttk.Button(add_record_frame, text="Submit", command=self.submit_record)
        self.submit_button.grid(row=5, column=1, sticky=tk.E, padx=20, pady=20)

    def create_visualization_tab(self):
        visualization_frame = ttk.Frame(self.notebook)
        self.notebook.add(visualization_frame, text="Visualization")

        self.income_expense_pie_chart_button = ttk.Button(visualization_frame, text="Income vs Expense Pie Chart",
                                                          command=plot_income_expense_pie_chart)
        self.income_expense_pie_chart_button.pack(pady=20)

        self.income_category_pie_chart_button = ttk.Button(visualization_frame, text="Income by Category Pie Chart",
                                                           command=lambda: plot_category_pie_chart("income"))
        self.income_category_pie_chart_button.pack(pady=20)

        self.expense_category_pie_chart_button = ttk.Button(visualization_frame, text="Expense by Category Pie Chart",
                                                            command=lambda: plot_category_pie_chart("expense"))
        self.expense_category_pie_chart_button.pack(pady=20)

    def submit_record(self):
        record_type = self.record_type.get()
        category = self.category.get()
        amount_str = self.amount.get()
        date = self.date.get()
        note = self.note.get()

        if not amount_str:
            tk.messagebox.showerror("Error", "Amount field cannot be empty")
            return

        try:
            amount = float(amount_str)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid amount format")
            return

        if record_type == 'income':
            add_income(category, amount, date, note)
        else:
            add_expense(category, amount, date, note)

        self.clear_form()

    def clear_form(self):
        self.record_type.current(0)
        self.category.current(0)
        self.amount.delete(0, tk.END)
        self.date.delete(0, tk.END)
        self.note.delete(0, tk.END)


if __name__ == "__main__":
    data_manager.create_database()
    app = Application()
    app.mainloop()
