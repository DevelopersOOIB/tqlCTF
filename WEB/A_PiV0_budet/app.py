from flask import Flask, jsonify, request, render_template
import json
import os
import sqlite3

app = Flask(__name__)

def create_database():
    if not os.path.exists('database.db'):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE drinks
                     (id INTEGER PRIMARY KEY, type TEXT, brand TEXT, amount INTEGER)''')
        c.execute('''CREATE TABLE personal
                     (id INTEGER PRIMARY KEY, author TEXT, channel TEXT)''')
        c.execute('''CREATE TABLE flag31337
                     (id INTEGER PRIMARY KEY, flag_value_tql_ctf TEXT)''')
        drinks = [
            ('Beer', 'Kronenbourg', 1664),
            ('Whisky', 'Makers Mark', 150),
            ('Vodka', 'Absolut', 12)
        ]
        c.executemany("INSERT INTO drinks (type, brand, amount) VALUES (?, ?, ?)", drinks)
        c.execute("INSERT INTO personal (id, author, channel) VALUES (1337, 'cherepawwka', 'https://t.me/CherepawwkaChannel')")
        c.execute("INSERT INTO flag31337 (id, flag_value_tql_ctf) VALUES (777, 'tqlCTF{P3Y73_P1V0_P3NN03_-_8UD37_J1ZN_07M3NN4Y4}')")
        conn.commit()
        conn.close()
    else:
        print("Database exists")


def get_drinks():
    with open('drinks.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/styles.css')
def styles():
    return app.send_static_file('styles.css')

@app.route('/api/v0.0/drinks', methods=['GET'])
def get_all_drinks_sql():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    query = "SELECT * FROM drinks"
    c.execute(query)
    drinks = c.fetchall()
    conn.close()
    drinks_list = []
    for drink in drinks:
        drink_dict = {
            'id': drink[0],
            'type': drink[1],
            'brand': drink[2],
            'amount': drink[3]
        }
        drinks_list.append(drink_dict)
    return jsonify(drinks_list)

@app.route('/api/v0.0/drinks/search', methods=['GET'])
def search_drinks_sql():
    query = request.args.get('query', '').lower()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    sql_query = "SELECT * FROM drinks WHERE type LIKE '%" + query + "%' OR brand LIKE '%" + query + "%'"
    c.execute(sql_query)
    drinks = c.fetchall()
    conn.close()
    filtered_drinks = []
    for drink in drinks:
        drink_dict = {
            'id': drink[0],
            'type': drink[1],
            'brand': drink[2],
            'amount': drink[3]
        }
        filtered_drinks.append(drink_dict)
    return jsonify(filtered_drinks)

@app.route('/api/v1.0/drinks', methods=['GET'])
def get_all_drinks_json():
    drinks = get_drinks()
    return jsonify(drinks)

@app.route('/api/v1.0/drinks/search', methods=['GET'])
def search_drinks_json():
    query = request.args.get('query', '').lower()
    drinks = get_drinks()
    filtered_drinks = [drink for drink in drinks if query in drink['type'].lower() or query in drink['brand'].lower()]
    return jsonify(filtered_drinks)

if __name__ == '__main__':
    create_database()
    app.run(host="0.0.0.0", port=80)
