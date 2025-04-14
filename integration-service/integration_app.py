from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
MYSQL_HOST = "mooninsurance.ctuswk86cwot.eu-north-1.rds.amazonaws.com"
MYSQL_USER = "admin"
MYSQL_PWD = "root0811"
MYSQL_DB = "mooninsurance"
PORT = "3306"

@app.route('/integration')
def index():
    return render_template('index.html')

# CREATE: Add a new sale
@app.route('/integration/add', methods=['POST'])
def add_sale():
    data = request.json
    print("Received Agent Data:", data)
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST, user=MYSQL_USER,
            password=MYSQL_PWD, database=MYSQL_DB, port=PORT
        )
        cursor = connection.cursor()

        query = """
        INSERT INTO sales (agent_code, product_id, amount, sale_date, branch)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data.get('agent_code'),
            data.get('product_id'),
            data.get('amount'),
            data.get('sale_date'),
            data.get('branch')
        ))
        connection.commit()
        return jsonify({"message": "Sale record added successfully."}), 201

    except mysql.connector.Error as err:
        print("[ERROR - AGENT ADD]:", err)  # 👈 log MySQL error
        return jsonify({"message": "Failed to add sale record."}), 500

# READ: Get all sales
@app.route('/integration/get', methods=['GET'])
def get_sales():
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST, user=MYSQL_USER,
            password=MYSQL_PWD, database=MYSQL_DB, port=PORT
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM sales")
        sales = cursor.fetchall()

        return jsonify(sales), 200

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"message": "Failed to retrieve sales."}), 500

# UPDATE: Update a sale record
@app.route('/integration/update/<int:sale_id>', methods=['PUT'])
def update_sale(sale_id):
    data = request.json
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST, user=MYSQL_USER,
            password=MYSQL_PWD, database=MYSQL_DB, port=PORT
        )
        cursor = connection.cursor()

        query = """
        UPDATE sales
        SET agent_code = %s, product_id = %s, amount = %s, sale_date = %s, branch = %s
        WHERE sale_id = %s
        """
        cursor.execute(query, (
            data.get('agent_code'),
            data.get('product_id'),
            data.get('amount'),
            data.get('sale_date'),
            data.get('branch'),
            sale_id
        ))
        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Sale record not found."}), 404

        return jsonify({"message": "Sale record updated successfully."}), 200

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"message": "Failed to update sale record."}), 500

# DELETE: Delete a sale
@app.route('/integration/delete/<int:sale_id>', methods=['DELETE'])
def delete_sale(sale_id):
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST, user=MYSQL_USER,
            password=MYSQL_PWD, database=MYSQL_DB, port=PORT
        )
        cursor = connection.cursor()

        cursor.execute("DELETE FROM sales WHERE sale_id = %s", (sale_id,))
        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Sale record not found."}), 404

        return jsonify({"message": "Sale record deleted successfully."}), 200

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"message": "Failed to delete sale."}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
