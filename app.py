from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from pathlib import Path

app = Flask(__name__)
app.secret_key = "change-this-secret-key"
DB_PATH = Path("portfolio.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all fields.", "error")
        return redirect(url_for("home") + "#contact")

    if len(name) > 80 or len(email) > 120 or len(message) > 2000:
        flash("Your message is too long. Please shorten it.", "error")
        return redirect(url_for("home") + "#contact")

    with get_db() as conn:
        conn.execute(
            "INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
            (name, email, message)
        )

    flash("Thanks! Your message was saved successfully.", "success")
    return redirect(url_for("home") + "#contact")

@app.route("/admin/messages")
def admin_messages():
    # Local demo page only. Add proper authentication before deploying publicly.
    with get_db() as conn:
        messages = conn.execute(
            "SELECT name, email, message, created_at FROM messages ORDER BY id DESC"
        ).fetchall()
    return render_template("messages.html", messages=messages)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
