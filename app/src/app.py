from flask import Flask, jsonify, request
import os
import mysql.connector

app = Flask(__name__)

# DB Configuration
db_config = {
    'user': os.environ.get('DB_USERNAME'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST'),
    'database': os.environ.get('DB_DEFAULT_DATABASE')
}

@app.route('/getuser', methods=['GET'])
def get_user():
    try:
        cursor = None  
        conn = None 
        user_id = request.args.get('id')
        print(f"user_id is {user_id}")
        conn = mysql.connector.connect(**db_config)
        print(f"After")
        cursor = conn.cursor()
        query = "SELECT * FROM user_details WHERE id = %s"
        cursor.execute(query, (user_id,)) 
        user = cursor.fetchone()
        if user:
            user_details = {
                'id': user[0],
                'username': user[1],
                'email': user[2]
            }
            return jsonify(user_details)
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'message': 'An error occurred'}), 500
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
