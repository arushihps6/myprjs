from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='db'
        )
        if connection.is_connected():
            print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search_employee():
    ename = request.args.get('ename')
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM empl WHERE ename = %s"
    cursor.execute(query, (ename,))
    records = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(records)

@app.route('/insert', methods=['POST'])
def insert_employee():
    data = request.json
    ename = data['ename']
    connection = create_connection()
    cursor = connection.cursor()
    query = "INSERT INTO empl (ename) VALUES (%s)"
    cursor.execute(query, (ename,))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({'message': 'Employee added successfully'}), 201

@app.route('/display', methods=['GET'])
def display_all_employees():
    connection = create_connection()
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM empl"
    cursor.execute(query)
    records = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(records)

if __name__ == '__main__':
   app.run(debug=True)
