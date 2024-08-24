from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('medications.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM medications WHERE name LIKE ? OR formula LIKE ?',
                        ('%' + query + '%', '%' + query + '%')).fetchone()
    conn.close()
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
