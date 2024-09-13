import sqlite3


def create_database():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute('DROP TABLE IF EXISTS uploads')
    conn.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT NOT NULL,
            password TEXT NOT NULL  
        )               
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            filename TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    cursor.execute(
        'INSERT INTO users (login, password) VALUES (?, ?)', 
        ('admin', '93a0aac1-e458-4f2d-aa42-e947c17b0c82')
    )
    
    cursor.execute(
        'INSERT INTO uploads (user_id, filename) VALUES (?, ?)', 
        (1, '/static/uploads/93a0aac1-e458-4f2d-aa42-e947c17b0c82.jpg',)
    )

    conn.commit()
    conn.close()


def register(login, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT * FROM users WHERE login = ?', 
        (login,)
    )
    user = cursor.fetchone()

    if user:
        return False
    
    cursor.execute(
        'INSERT INTO users (login, password) VALUES (?, ?)', 
        (login, password,)
    )

    conn.commit()
    conn.close()
    
    return True


def login(login, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT * FROM users WHERE login = ? AND password = ?', 
        (login,password)
    )

    user = cursor.fetchone()
    conn.close()
    return user


def change_pass(login, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE users SET password = ? WHERE login = ?',
        (password, login)
    )

    conn.commit()
    conn.close()



def check_login(login):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT * FROM users WHERE login = ?', 
        (login,)
    )

    user = cursor.fetchone()
    conn.close()
    return user


def get_username_by_id(id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    cursor.execute(
        'SELECT * FROM users WHERE id = ?', 
        (id,)
    )

    user = cursor.fetchone()
    conn.close()
    return user


def add_uploaded_file(user_id, filename):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO uploads (user_id, filename) VALUES (?, ?)', 
        (user_id, filename,)
    )   

    conn.commit()
    conn.close()


def get_uploads_by_user_id(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute(
        'SELECT filename FROM uploads WHERE user_id = ?',
        (user_id,)
    )

    fetchall = cursor.fetchall()
    conn.close()

    uploads = []
    
    for i in fetchall:
        uploads.append(i[0])

    return uploads

    