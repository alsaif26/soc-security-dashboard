from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'soc_secret_key'

users = {
    'admin': 'password123',
    'safu': '1234'
}

def init_db():
    conn = sqlite3.connect('soc.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS alerts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        severity TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        severity TEXT NOT NULL,
        status TEXT DEFAULT 'Open',
        reported_by TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )''')
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect('soc.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password!'
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    alerts = conn.execute('SELECT * FROM alerts ORDER BY timestamp DESC').fetchall()
    conn.close()
    return render_template('dashboard.html', user=session['user'], alerts=alerts)

@app.route('/add_alert', methods=['POST'])
def add_alert():
    if 'user' not in session:
        return redirect(url_for('login'))
    title = request.form['title']
    severity = request.form['severity']
    conn = get_db()
    conn.execute('INSERT INTO alerts (title, severity) VALUES (?, ?)', (title, severity))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/delete_alert/<int:id>')
def delete_alert(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    conn.execute('DELETE FROM alerts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('dashboard'))

@app.route('/incidents')
def incidents():
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    incidents = conn.execute('SELECT * FROM incidents ORDER BY timestamp DESC').fetchall()
    conn.close()
    return render_template('incidents.html', user=session['user'], incidents=incidents)

@app.route('/add_incident', methods=['POST'])
def add_incident():
    if 'user' not in session:
        return redirect(url_for('login'))
    title = request.form['title']
    description = request.form['description']
    severity = request.form['severity']
    conn = get_db()
    conn.execute('INSERT INTO incidents (title, description, severity, reported_by) VALUES (?, ?, ?, ?)',
                 (title, description, severity, session['user']))
    conn.commit()
    conn.close()
    return redirect(url_for('incidents'))

@app.route('/close_incident/<int:id>')
def close_incident(id):
    if 'user' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    conn.execute("UPDATE incidents SET status='Closed' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('incidents'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)