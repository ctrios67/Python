#! /usr/bin/env python3
import sqlite3

def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)')
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO book VALUES (NULL, ?, ?, ?, ?)', (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()
    conn.close()
    return rows

# We need to set our parameters to some defaults here in case the user only enters one search term
# Otherwise we'd get an error.
def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?', (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

# Grab the list selection from the listbox as a tuple
# This realistically would have the id extracted from a tuple
def delete(id):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM book WHERE id=?', (id,))
    conn.commit()
    conn.close()

# Similar process to delete
def update(id, title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cursor()
    cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
#insert('The Gunslinger', 'Stephen Hawking', 2009, 22312312312 )
#delete(3)
#print(view())
#print(search(author='John Smith'))
#update(3, 'The Gunslinger', 'Stephen Hawking', 2009, 99999)
#print(view())
