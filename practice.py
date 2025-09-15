from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Balaji@123",
    database="school"
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS studying (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
)
""")

@app.route('/')
def index():
    cursor.execute("SELECT * FROM studying")
    students = cursor.fetchall()
    return render_template("index.html", students=students)

@app.route('/add', methods=["POST"])
def add():
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']
    query = "INSERT INTO studying (name, age, grade) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, grade))
    conn.commit()
    return redirect('/')

@app.route('/delete/<int:student_id>')
def delete(student_id):
    query = "DELETE FROM studying WHERE id=%s"
    cursor.execute(query, (student_id,))
    conn.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
