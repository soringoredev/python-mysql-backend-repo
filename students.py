from db import cursor, connection

def create_student(name):
    query = 'INSERT INTO students (name) VALUES(%s)'
    cursor.execute(query, (name,))
    connection.commit()

def get_students():
    cursor.execute('SELECT * FROM students')
    return cursor.fetchall()

def hakuna_matata():
    print('zdarova')

def hakuna_matata2():
    print('zdarova2')