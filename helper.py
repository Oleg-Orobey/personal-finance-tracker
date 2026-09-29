import sqlite3
import datetime
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db', 'database.db')

with sqlite3.connect(DB_PATH) as db:
    cursor = db.cursor()

def get_statistic_data():
    all_data = []
    with sqlite3.connect(DB_PATH) as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """SELECT * FROM payments JOIN expenses
        ON expenses.id = payments.expense_id """
        cursor.execute(query)
        all_data = cursor
    return all_data

def get_most_common_item():
    data = get_statistic_data()
    quantity = {}
    for payments in data:
        if payments['expense_id'] in quantity:
            quantity[payments['expense_id']] ['qty'] += 1 
        else:
            quantity[payments['expense_id']] = {'qty': 1, 'name':payments['name']}
    return max(quantity.values(), key=lambda x: x['qty'])['name']       

def get_most_exp_item():
    data = get_statistic_data()
    return max(list(data), key=lambda x: x['amount'])['name']

def get_most_exp():
    data = get_statistic_data()
    return sum(payments['amount'] for payments in data)


def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

def get_timestamp_from_strings(s):
    t = s.split('-')
    return get_timestamp(int(t[2]),int(t[1]),int(t[0]))
    

with sqlite3.connect(DB_PATH) as db:
    cursor = db.cursor()
    query = """ SELECT * FROM payments"""
    #cursor.execute(query)
    
    
def get_table_data():
    data = get_statistic_data()
    return [(i['id'],i['name'],i['amount'],'{:%d-%m-%Y}'.format(
                    get_date(i['payment_data']))) for i in data]
        
def get_all_expenses_items():
    all_data = {'accordance': {}, 'names':[] }
    result = {}
    with sqlite3.connect(DB_PATH) as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """ SELECT id, name FROM expenses """
        cursor.execute(query)
        result = dict(cursor)
        all_data['accordance'] = {result[k]:k for k in result}
        all_data["names"] = [v for v in result.values()]
    return all_data

def get_statistic_data1():
    all_data1 = []
    with sqlite3.connect(DB_PATH) as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """SELECT * FROM payments1 JOIN expenses1
        ON expenses1.id = payments1.expense_id """
        cursor.execute(query)
        all_data1 = cursor
    return all_data1

def get_most_common_item1():
    data1 = get_statistic_data1()
    quantity = {}
    for payments1 in data1:
        if payments1['expense_id'] in quantity:
            quantity[payments1['expense_id']] ['qty'] += 1 
        else:
            quantity[payments1['expense_id']] = {'qty': 1, 'name':payments1['name']}
    return max(quantity.values(), key=lambda x: x['qty'])['name']       

def get_most_exp_item1():
    data1 = get_statistic_data1()
    return max(list(data1), key=lambda x: x['amount'])['name']

def get_most_exp1():
    data = get_statistic_data1()
    return sum(payments1['amount'] for payments1 in data)


def get_timestamp1(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))

def get_date1(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

def get_timestamp_from_strings1(s):
    t = s.split('-')
    return get_timestamp1(int(t[2]),int(t[1]),int(t[0]))
    

with sqlite3.connect(DB_PATH) as db:
    cursor = db.cursor()
    query = """ SELECT * FROM payments1"""
    #cursor.execute(query)
    
    
def get_table_data1():
    data1 = get_statistic_data1()
    return [(i['id'],i['name'],i['amount'],'{:%d-%m-%Y}'.format(
                    get_date(i['payment_data']))) for i in data1]
        
def get_all_expenses_items1():
    all_data1 = {'accordance': {}, 'names':[] }
    result = {}
    with sqlite3.connect(DB_PATH) as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """ SELECT id, name FROM expenses1 """
        cursor.execute(query)
        result = dict(cursor)
        all_data1['accordance'] = {result[k]:k for k in result}
        all_data1["names"] = [v for v in result.values()]
    return all_data1

