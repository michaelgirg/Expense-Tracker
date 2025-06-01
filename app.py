from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize DB
def init_db():
    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            amount REAL,
            category TEXT
        )''')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_expense():
    data = request.json
    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO expenses (title, amount, category) VALUES (?, ?, ?)",
                  (data['title'], data['amount'], data['category']))
        conn.commit()
    return jsonify({'status': 'success'})

@app.route('/expenses', methods=['GET'])
def get_expenses():
    with sqlite3.connect("database.db") as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM expenses")
        rows = c.fetchall()
    return jsonify(rows)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
