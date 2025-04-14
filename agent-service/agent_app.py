from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

# Database connection configuration
MYSQL_HOST = "mooninsurance.ctuswk86cwot.eu-north-1.rds.amazonaws.com"
MYSQL_USER = "admin"
MYSQL_PWD = "root0811"
MYSQL_DB = "mooninsurance"
PORT = "3306"

# Route for the front-end page
@app.route('/agent')
def index():
    return render_template('index.html')

# API to add a new agent
@app.route('/agent/add', methods=['POST'])
def add_agent():
    data = request.json
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            port=PORT
        )
        cursor = connection.cursor()

        query = """
        INSERT INTO agents (agent_code, first_name, last_name, branch, contact_number, email, team, hire_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            data.get('agent_code'),
            data.get('first_name'),
            data.get('last_name'),
            data.get('branch'),
            data.get('contact_number'),
            data.get('email'),
            data.get('team'),
            data.get('hire_date')
        ))
        connection.commit()

        return jsonify({"message": "Agent added successfully."}), 201

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"message": "Failed to add agent."}), 500

# API to get all agents
@app.route('/agent/get', methods=['GET'])
def get_agents():
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            port=PORT
        )
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM agents")
        agents = cursor.fetchall()

        return jsonify(agents), 200

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"message": "Failed to retrieve agents."}), 500

# API to update an agent
@app.route('/agent/update/<int:agent_id>', methods=['PUT'])
def update_agent(agent_id):
    data = request.json
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            port=PORT
        )
        cursor = connection.cursor()

        query = """
        UPDATE agents
        SET agent_code = %s, first_name = %s, last_name = %s, branch = %s,
            contact_number = %s, email = %s, team = %s, hire_date = %s
        WHERE agent_id = %s
        """
        cursor.execute(query, (
            data.get('agent_code'),
            data.get('first_name'),
            data.get('last_name'),
            data.get('branch'),
            data.get('contact_number'),
            data.get('email'),
            data.get('team'),
            data.get('hire_date'),
            agent_id
        ))
        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Agent not found."}), 404

        return jsonify({"message": "Agent updated successfully."}), 200

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"message": "Failed to update agent."}), 500

# API to delete an agent
@app.route('/agent/delete/<int:agent_id>', methods=['DELETE'])
def delete_agent(agent_id):
    try:
        connection = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            port=PORT
        )
        cursor = connection.cursor()

        cursor.execute("DELETE FROM agents WHERE agent_id = %s", (agent_id,))
        connection.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Agent not found."}), 404

        return jsonify({"message": "Agent deleted successfully."}), 200

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return jsonify({"message": "Failed to delete agent."}), 500

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
