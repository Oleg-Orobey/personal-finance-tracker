import tkinter as tk 
from tkinter import ttk
import helper as eh
import sqlite3

root = tk.Tk()
root.title("Финансы")


frame_1 = tk.Frame(root, bg="#E0FFFF")
frame_2 = tk.Frame(root, bg="#84c2c2")
frame_3 = tk.Frame(root,bg="#84c2c2")
frame_4 = tk.Frame(root,bg="#84c2c2")

frame_1.grid(row=0, column=1, sticky='we ns')
frame_2.grid(row=1, column=0, sticky="w")
frame_3.grid(row=0, column=0, sticky='we ns')
frame_4.grid(row=1, column=1)


items = eh.get_all_expenses_items()


def form_submit():
    amount = float(f_amount.get())
    expense_id = items['accordance'][f_choose.get()]
    insert_payment = (amount, expense_id)
    
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ INSERT INTO payments(amount, expense_id, payment_data)
                                        VALUES (?,?,3123123123);"""
        cursor.execute(query, insert_payment)
        db.commit()

l_choose = ttk.Label(frame_3, text='Выберите статью расходов', font='17', background='#84c2c2')
f_choose = ttk.Combobox(frame_3, values=items['names'])
l_amount = ttk.Label(frame_3, text='Добавить расход', font='17', background='#84c2c2')
f_amount = ttk.Entry(frame_3, justify=tk.RIGHT)
btn_submit = ttk.Button(frame_3, text='Добавить', command=form_submit)

l_choose.grid(row=0, column=0, sticky='w', padx=20, pady=40)
f_choose.grid(row=0, column=1, sticky='e', padx=20, pady=50)
l_amount.grid(row=2, column=0, sticky='w', padx=20, pady=10)
f_amount.grid(row=2, column=1, sticky='e', padx=10, pady=10)
btn_submit.grid(row=3, column=0, sticky='n', padx=10, pady=10, columnspan=2)

l_cost = tk.Label(frame_3, text="Расход", font="helvetica 12 bold", width=12, bg="#84c2c2")
l_cost1 = tk.Label(frame_3, text=eh.get_most_exp(),font="helvetica 12 bold", width=12, bg="#84c2c2")

l_cost.grid(row=6, column=0, sticky="w", padx=10, pady=10)
l_cost1.grid(row=6, column=1, sticky="e", padx=10, pady=10, columnspan=1)

most_common = tk.Label(frame_3, text="Самая популярная категория",bg="#84c2c2", font='17')
most_exp = tk.Label(frame_3, text="Самая дорогая категория",bg="#84c2c2", font='17')
most_common1 = tk.Label(frame_3, text=eh.get_most_common_item(),bg="#84c2c2", font='17')
most_exp1 = tk.Label(frame_3, text=eh.get_most_exp_item(),  bg="#84c2c2", font='17')

most_common.grid(row=4, column=0,sticky="w", padx=10, pady=10)
most_common1.grid(row=4, column=1,sticky="e", padx=10, pady=10)
most_exp.grid(row=5, column=0,sticky="w", padx=10, pady=10)
most_exp1.grid(row=5, column=1,sticky="e", padx=10, pady=10)

heads = [  '№', 'Категория', 'Сумма']
table = ttk.Treeview(frame_2, show='headings')
table['columns'] = heads

for header in heads:
    table.heading(header, text=header, anchor='center')
    table.column(header, anchor='center')

for row in eh.get_table_data():
    table.insert('', tk.END, values=row)
    
scroll_pane = ttk.Scrollbar(frame_2, command=table.yview)
table.configure(yscrollcommand=scroll_pane.set)

scroll_pane.pack(side=tk.RIGHT, fill=tk.Y)
table.pack(expand=tk.YES, fill=tk.BOTH)
items1 = eh.get_all_expenses_items1()

def form_submit1():
    amount = float(f_amount1.get())
    expense_id = items1['accordance'][f_choose1.get()]
    insert_payment1 = (amount, expense_id)
    
    with sqlite3.connect('db/database.db') as db:
        cursor = db.cursor()
        query = """ INSERT INTO payments1(amount, expense_id, payment_data)
                                        VALUES (?,?,3123123123);"""
        cursor.execute(query, insert_payment1)
        db.commit()
        
l_choose1 = ttk.Label(frame_1, text='Выберите вариант дохода', font='17', background='#E0FFFF')
f_choose1 = ttk.Combobox(frame_1, values=items1['names'])
l_amount1 = ttk.Label(frame_1, text='Добавить расход', font='17', background='#E0FFFF')
f_amount1 = ttk.Entry(frame_1, justify=tk.RIGHT)
btn_submit1 = ttk.Button(frame_1, text='Добавить', command=form_submit1)


l_choose1.grid(row=0, column=0, sticky='w', padx=20, pady=40)
f_choose1.grid(row=0, column=1, sticky='e', padx=20, pady=50)
l_amount1.grid(row=2, column=0, sticky='w', padx=20, pady=10)
f_amount1.grid(row=2, column=1, sticky='e', padx=10, pady=10)
btn_submit1.grid(row=3, column=0, sticky='n', padx=10, pady=10, columnspan=2)


most_common1 = tk.Label(frame_1, text="Самая популярная категория",bg="#E0FFFF", font='17')
most_exp1 = tk.Label(frame_1, text="Самая дорогая категория",bg="#E0FFFF", font='17')
most_common11 = tk.Label(frame_1, text=eh.get_most_common_item1(),bg="#E0FFFF", font='17')
most_exp11 = tk.Label(frame_1, text=eh.get_most_exp_item1(),  bg="#E0FFFF", font='17')

most_common1.grid(row=4, column=0,sticky="w", padx=10, pady=10)
most_common11.grid(row=4, column=1,sticky="e", padx=10, pady=10)
most_exp1.grid(row=5, column=0,sticky="w", padx=10, pady=10)
most_exp11.grid(row=5, column=1,sticky="e", padx=10, pady=10)

l_cost1 = tk.Label(frame_1, text="Доход", font="helvetica 12 bold", width=12, bg="#E0FFFF")
l_cost11 = tk.Label(frame_1, text=eh.get_most_exp1(),font="helvetica 12 bold", width=12, bg="#E0FFFF")

l_cost1.grid(row=6, column=0, sticky="w", padx=10, pady=10)
l_cost11.grid(row=6, column=1, sticky="e", padx=10, pady=10, columnspan=1)


heads = ['№','Категория','Сумма']
table1 = ttk.Treeview(frame_4, show='headings')
table1 ['columns'] = heads 

for header in heads:
    table1.heading(header, text=header, anchor='center')
    table1.column(header, anchor='center')
    
for row in eh.get_table_data1():
    table1.insert('', tk.END, values=row)

scroll_pane1 = ttk.Scrollbar(frame_4, command=table.yview)
table1.configure(yscrollcommand=scroll_pane1.set)
scroll_pane1.pack(side=tk.RIGHT, fill=tk.Y)
table1.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()

