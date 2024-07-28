import sqlite3
from datetime import datetime
def connection():
    connection=sqlite3.connect('todo.db')
    return connection
def select_event():
    conn = connection()
    cursor=conn.cursor()
    cursor.execute("SELECT id,event,IM,Pt FROM tasks ")
    records=cursor.fetchall()
    conn.close()
    return records
def select_edit(id):
    conn = connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM tasks where id=?",(id,))
    records=cursor.fetchall()
    conn.close()
    return records
def save_data(event,description,due_date,status,IM,Pt):
    conn = connection()
    cursor=conn.cursor()
    cursor.execute('INSERT INTO tasks(event,description,due_date,status,IM,Pt)VALUES(?,?,?,?,?,?)',(event,description,due_date,status,IM,Pt))
    conn.commit()
    conn.close()
def update_due():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id,due_date FROM tasks")
    records=cursor.fetchall()
    for record in records:
        id=record[0]
        due_date=record[1]

        due_time=datetime.strptime(due_date,'%Y-%m-%d %H:%M')
        remaining_time=(due_time -datetime.now()).days
        cursor.execute("UPDATE tasks SET Pt = ? WHERE id = ?", (remaining_time, id))
    conn.commit()
    conn.close()
def update_record(id,event,description,due_date,status,IM,Pt):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET event=?,description=?,due_date=?,status=?,IM=?,Pt=?WHERE id=?',
                   (event, description, due_date, status, IM, Pt,id))
    conn.commit()
    conn.close()
def delete_record(id):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print("删除成功")