import requests

def test_agent_service():
    print("🔧 Testing Agent Service CRUD")

    # CREATE
    agent_data = {
        "agent_code": "AGT999",
        "first_name": "Test",
        "last_name": "Agent",
        "branch": "Colombo",
        "contact_number": "0777000000",
        "email": "test.agent@example.com",
        "product_types": "Life, Health",
        "hire_date": "2024-01-01"
    }
    r = requests.post("http://localhost:5000/agent/add", json=agent_data)
    print("Create Agent:", r.status_code, r.json())

    # READ
    r = requests.get("http://localhost:5000/agent/get")
    agents = r.json()
    print("Read Agents:", r.status_code)
    agent_id = agents[-1]["agent_id"]  # Get last inserted

    # UPDATE
    update_data = {
        "agent_code": "AGT999",
        "first_name": "Updated",
        "last_name": "Agent",
        "branch": "Kandy",
        "contact_number": "0777123456",
        "email": "updated.agent@example.com",
        "product_types": "Life",
        "hire_date": "2024-02-01"
    }
    r = requests.put(f"http://localhost:5000/agent/update/{agent_id}", json=update_data)
    print("Update Agent:", r.status_code, r.json())

    # DELETE
    r = requests.delete(f"http://localhost:5000/agent/delete/{agent_id}")
    print("Delete Agent:", r.status_code, r.json())

def test_integration_service():
    print("\n🔧 Testing Integration Service CRUD")

    # CREATE
    sale_data = {
        "agent_code": "AGT123",  # Ensure this exists in your DB
        "product_name": "Health Insurance",
        "amount": 120000.50,
        "sale_date": "2024-03-01",
        "branch": "Galle"
    }
    r = requests.post("http://localhost:5001/integration/add", json=sale_data)
    print("Create Sale:", r.status_code, r.json())

    # READ
    r = requests.get("http://localhost:5001/integration/get")
    sales = r.json()
    print("Read Sales:", r.status_code)
    sale_id = sales[-1]["sale_id"]  # Get last inserted

    # UPDATE
    update_data = {
        "agent_code": "AGT123",
        "product_name": "Life Insurance",
        "amount": 150000.00,
        "sale_date": "2024-03-10",
        "branch": "Matara"
    }
    r = requests.put(f"http://localhost:5001/integration/update/{sale_id}", json=update_data)
    print("Update Sale:", r.status_code, r.json())

    # DELETE
    r = requests.delete(f"http://localhost:5001/integration/delete/{sale_id}")
    print("Delete Sale:", r.status_code, r.json())

if __name__ == "__main__":
    test_agent_service()
    test_integration_service()
