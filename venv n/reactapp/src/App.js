from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="db"
)

@app.route('/search', methods=['GET'])
def search_employee():
    ename = request.args.get('ename')
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empl WHERE ename = %s", (ename,))
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

@app.route('/insert', methods=['POST'])
def insert_employee():
    ename = request.json.get('ename')
    cursor = db.cursor()
    cursor.execute("INSERT INTO empl (ename) VALUES (%s)", (ename,))
    db.commit()
    cursor.close()
    return jsonify({"message": "Employee added successfully"}), 201

@app.route('/get_all_employees', methods=['GET'])
def get_all_employees():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM empl")
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
