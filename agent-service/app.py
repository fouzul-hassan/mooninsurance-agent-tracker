from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate a basic in-memory database
agents = {}

@app.route("/agents", methods=["POST"])
def create_agent():
    data = request.get_json()
    agent_code = data.get("agent_code")
    if not agent_code:
        return jsonify({"error": "Agent code required"}), 400
    agents[agent_code] = data
    return jsonify({"message": "Agent created", "agent": data}), 201

@app.route("/agents/<agent_code>", methods=["GET"])
def get_agent(agent_code):
    agent = agents.get(agent_code)
    if not agent:
        return jsonify({"error": "Agent not found"}), 404
    return jsonify(agent)

@app.route("/agents/<agent_code>", methods=["PUT"])
def update_agent(agent_code):
    if agent_code not in agents:
        return jsonify({"error": "Agent not found"}), 404
    agents[agent_code].update(request.get_json())
    return jsonify({"message": "Agent updated", "agent": agents[agent_code]}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
