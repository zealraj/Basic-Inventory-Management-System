import sqlite3

def connect():

    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER,uqn INTEGER)")
    conn.commit()
    conn.close()

def insert_data(title,author,year,uqn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",(title,author,year,uqn))
    conn.commit()
    conn.close()

def view_data():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search_data(title="",author="",year="",uqn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? or author=? or year=? or uqn=?",(title,author,year,uqn))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_data(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update_data(id,title,author,year,uqn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,uqn=? WHERE id=?",(title,author,year,uqn,id))
    conn.commit()
    conn.close()

connect()
#insert_data("Python-New Gen","McD Berg",2019,91112256)
#delete_data(1)
#print(view_data())
#print(search_data(year=2019))


