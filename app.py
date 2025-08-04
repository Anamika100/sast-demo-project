import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    # ❌ Vulnerable: SQL Injection risk
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)
