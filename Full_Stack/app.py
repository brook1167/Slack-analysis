from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app) 
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345q',
    'database': 'employees',
}


@app.route('/api/data')
def get_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT id, name FROM users')
        data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        print('Error fetching data:', e)
        return jsonify({'error': 'Internal Server Error'}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
