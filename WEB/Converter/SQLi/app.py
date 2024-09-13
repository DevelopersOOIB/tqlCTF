import sqlite3
from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    if request.args.get('number'):
        try:
            if validate_ticket(request.args.get('number')):
                success = "Ticket is valid"
                return render_template('tickets.html', success=success)
            
            error = "Ticket is invalid"
            return render_template('tickets.html', error=error)
        except Exception as e:
            print(e)
            error = "Internal error"
            return render_template('tickets.html', error=error)

    return render_template('tickets.html')


def init_database():
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS tickets')
    cursor.execute('DROP TABLE IF EXISTS tqlCTF')

    cursor.execute('''
       CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticket_number TEXT NOT NULL
        )         
    ''')

    cursor.execute('''
       CREATE TABLE IF NOT EXISTS tqlCTF (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            flag TEXT NOT NULL
        )         
    ''')

    for i in range(1234, 1249):
        cursor.execute(
            'INSERT INTO tickets (ticket_number) VALUES (?)',
            (str(i),)
        )

    cursor.execute(
        'INSERT INTO tqlCTF (flag) VALUES (?)',
        ('tqlCTF{y0u_c4n_h4ck_1ntern4l_s3rv1c3_g00d_j0b}',)
    )

    conn.commit()
    conn.close()


def validate_ticket(ticket_number):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets WHERE ticket_number = '{}'".format(ticket_number))
    ticket = cursor.fetchone()
    conn.close()
    return ticket


if __name__ == '__main__':
    init_database()
    app.run(debug=True, port=5000, host='0.0.0.0')
