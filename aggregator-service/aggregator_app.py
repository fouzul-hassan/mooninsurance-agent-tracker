from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database configuration (AWS RDS)
MYSQL_HOST = "mooninsurance.ctuswk86cwot.eu-north-1.rds.amazonaws.com"
MYSQL_USER = "admin"
MYSQL_PWD = "root0811"
MYSQL_DB = "mooninsurance"
PORT = "3306"

@app.route('/aggregator')
def index():
    return render_template('index.html')

# Route: Total sales by agent
@app.route('/aggregator/sales-by-agent', methods=['GET'])
def get_sales_by_agent():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            port=PORT
        )
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT agent_code, SUM(amount) as total_sales
        FROM sales
        GROUP BY agent_code
        ORDER BY total_sales DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()

        return jsonify(results), 200

    except mysql.connector.Error as err:
        print("Error:", err)
        return jsonify({"message": "Failed to fetch sales summary"}), 500

# Route: Total sales by branch
@app.route('/aggregator/sales-by-branch', methods=['GET'])
def get_sales_by_branch():
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            port=PORT
        )
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT branch, SUM(amount) as total_sales
        FROM sales
        GROUP BY branch
        ORDER BY total_sales DESC
        """
        cursor.execute(query)
        results = cursor.fetchall()

        return jsonify(results), 200

    except mysql.connector.Error as err:
        print("Error:", err)
        return jsonify({"message": "Failed to fetch branch sales"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
