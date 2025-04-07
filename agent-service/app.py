from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://admin:root0811@mooninsurance-mysql.cn4e2eau6isn.ap-south-1.rds.amazonaws.com:3306/mooninsurance')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Agent(db.Model):
    agent_code = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    permitted_products = db.Column(db.String(255))

@app.route('/agents', methods=['GET'])
def get_agents():
    agents = Agent.query.all()
    return jsonify([{
        "agent_code": a.agent_code,
        "name": a.name,
        "branch": a.branch,
        "email": a.email,
        "phone": a.phone,
        "permitted_products": a.permitted_products
    } for a in agents])

@app.route('/agents', methods=['POST'])
def create_agent():
    data = request.get_json()
    agent = Agent(**data)
    db.session.add(agent)
    db.session.commit()
    return jsonify({"message": "Agent created"}), 201

@app.route('/agents/<agent_code>', methods=['GET'])
def get_agent(agent_code):
    agent = Agent.query.get(agent_code)
    if not agent:
        return jsonify({"error": "Agent not found"}), 404
    return jsonify({
        "agent_code": agent.agent_code,
        "name": agent.name,
        "branch": agent.branch,
        "email": agent.email,
        "phone": agent.phone,
        "permitted_products": agent.permitted_products
    })

@app.route('/agents/<agent_code>', methods=['PUT'])
def update_agent(agent_code):
    agent = Agent.query.get(agent_code)
    if not agent:
        return jsonify({"error": "Agent not found"}), 404
    for key, value in request.json.items():
        setattr(agent, key, value)
    db.session.commit()
    return jsonify({"message": "Agent updated"})

@app.route('/agents/<agent_code>', methods=['DELETE'])
def delete_agent(agent_code):
    agent = Agent.query.get(agent_code)
    if not agent:
        return jsonify({"error": "Agent not found"}), 404
    db.session.delete(agent)
    db.session.commit()
    return jsonify({"message": "Agent deleted"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
