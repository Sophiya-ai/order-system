import tkinter as tk
from tkinter import ttk
import sqlite3

def add_order():
    pass


# Создаём окошко интерфейса
app = tk.Tk()
app.title("Система управления заказами")

# Добавляем надписи, которые будут появляться в окошке. Используем функцию pack сразу,
# потому что надпись не нужно сохранять в переменную
tk.Label(app, text="Имя клиента").pack()

# Создаём поле для ввода имени клиента
customer_name_entry = tk.Entry(app)
customer_name_entry.pack()

# Создаём такие же поля для деталей заказа
tk.Label(app, text="Детали заказа").pack()
order_details_entry = tk.Entry(app)
order_details_entry.pack()

# Создаём кнопку, которая будет добавлять введённые данные в таблицу
add_button = tk.Button(app, text="Добавить заказ", command=add_order).pack()

# Используем функцию, чтобы создать таблицу из колонок, которые в ней размещены
columns = ("id", "customer_name", "order_details", "status")
tree = ttk.Treeview(app, columns=columns, show="headings")
for column in columns:
    tree.heading(column, text=column)
tree.pack()

app.mainloop()