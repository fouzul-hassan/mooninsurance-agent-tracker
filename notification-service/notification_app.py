from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
MYSQL_HOST = "mooninsurance.ctuswk86cwot.eu-north-1.rds.amazonaws.com"
MYSQL_USER = "admin"
MYSQL_PWD = "root0811"
MYSQL_DB = "mooninsurance"
PORT = "3306"

@app.route('/notification')
def index():
    return render_template('index.html')

# Send a notification
@app.route('/notification/send', methods=['POST'])
def send_notification():
    data = request.json
    agent_code = data.get("agent_code")
    message = data.get("message")

    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            port=PORT
        )
        cursor = connection.cursor()
        query = "INSERT INTO notifications (agent_code, message) VALUES (%s, %s)"
        cursor.execute(query, (agent_code, message))
        connection.commit()
        return jsonify({"message": f"Notification sent to agent {agent_code}."}), 201

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"message": "Failed to send notification."}), 500

# Get all notifications
@app.route('/notification/get', methods=['GET'])
def get_notifications():
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            port=PORT
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM notifications")
        records = cursor.fetchall()
        return jsonify(records), 200

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"message": "Failed to fetch notifications."}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
