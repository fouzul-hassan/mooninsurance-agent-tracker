import requests

# ========== Agent Service CRUD ==========
def test_agent_service():
    print("🧪 Testing Agent Service")

    # CREATE
    agent_data = {
        "agent_code": "AGT999",
        "first_name": "Test",
        "last_name": "Agent",
        "branch": "TestBranch",
        "contact_number": "0700000000",
        "email": "test@agent.com",
        "product_types": "TestProduct",
        "hire_date": "2025-01-01"
    }
    res = requests.post("http://localhost:5000/agent/add", json=agent_data)
    print("Create:", res.status_code, res.json())

    # READ
    res = requests.get("http://localhost:5000/agent/get")
    agents = res.json()
    agent_id = agents[-1]["agent_id"]
    print("Read:", res.status_code, f"Found {len(agents)} agents")

    # UPDATE
    update_data = agent_data.copy()
    update_data["first_name"] = "Updated"
    res = requests.put(f"http://localhost:5000/agent/update/{agent_id}", json=update_data)
    print("Update:", res.status_code, res.json())

    # DELETE
    res = requests.delete(f"http://localhost:5000/agent/delete/{agent_id}")
    print("Delete:", res.status_code, res.json())

# ========== Integration Service CRUD ==========
def test_integration_service():
    print("\n🧪 Testing Integration Service")

    # CREATE
    sale_data = {
        "agent_code": "AGT001",
        "product_name": "Testing Product",
        "amount": 99999.99,
        "sale_date": "2025-02-01",
        "branch": "TestBranch"
    }
    res = requests.post("http://localhost:5001/integration/add", json=sale_data)
    print("Create:", res.status_code, res.json())

    # READ
    res = requests.get("http://localhost:5001/integration/get")
    sales = res.json()
    sale_id = sales[-1]["sale_id"]
    print("Read:", res.status_code, f"Found {len(sales)} sales")

    # UPDATE
    update_data = sale_data.copy()
    update_data["amount"] = 88888.88
    res = requests.put(f"http://localhost:5001/integration/update/{sale_id}", json=update_data)
    print("Update:", res.status_code, res.json())

    # DELETE
    res = requests.delete(f"http://localhost:5001/integration/delete/{sale_id}")
    print("Delete:", res.status_code, res.json())

# ========== Notification Service CRUD ==========
def test_notification_service():
    print("\n🧪 Testing Notification Service")

    # CREATE
    note_data = {
        "agent_code": "AGT001",
        "message": "Test notification message"
    }
    res = requests.post("http://localhost:5002/notification/send", json=note_data)
    print("Create:", res.status_code, res.json())

    # READ
    res = requests.get("http://localhost:5002/notification/get")
    notes = res.json()
    note_id = notes[-1]["id"]
    print("Read:", res.status_code, f"Found {len(notes)} notifications")

    # NOTE: No update/delete implemented in notification_service (optional)

if __name__ == "__main__":
    test_agent_service()
    test_integration_service()
    test_notification_service()
