import requests

BASE_URL = "http://209.38.124.165.nip.io"  # Replace with your Ingress domain if needed

def test_agent_service():
    print("🧪 Testing Agent Service...")

    agent_payload = {
        "agent_code": "AGT999",
        "first_name": "Initial",
        "last_name": "Agent",
        "branch": "Kandy",
        "contact_number": "0779998888",
        "email": "init@moon.com",
        "team": "Beta",
        "hire_date": "2024-02-01"
    }

    # Create Agent
    res_add = requests.post(f"{BASE_URL}/agent/add", json=agent_payload)
    print("Create Agent:", res_add.status_code, res_add.text)

    # Fetch All Agents
    res_get = requests.get(f"{BASE_URL}/agent/get")
    print("Get Agents:", res_get.status_code)
    agents = res_get.json()
    agent_id = next((a['agent_id'] for a in agents if a['agent_code'] == 'AGT999'), None)

    # Update Agent
    if agent_id:
        updated_agent_payload = {
            "agent_code": "AGT999",
            "first_name": "Updated",
            "last_name": "AgentX",
            "branch": "Jaffna",
            "contact_number": "0712345678",
            "email": "updated.agent@moon.com",
            "team": "Gamma",
            "hire_date": "2024-05-01"
        }

        res_update = requests.put(f"{BASE_URL}/agent/update/{agent_id}", json=updated_agent_payload)
        print("Update Agent:", res_update.status_code, res_update.text)

        res_delete = requests.delete(f"{BASE_URL}/agent/delete/{agent_id}")
        print("Delete Agent:", res_delete.status_code, res_delete.text)
    else:
        print("Agent not found for update/delete")

def test_integration_service():
    print("\n🧪 Testing Integration Service...")

    sale_payload = {
        "agent_code": "AGT001",  
        "product_id": 1,        
        "amount": 78910.11,
        "sale_date": "2025-04-18",
        "branch": "Galle"
    }

    # Create Sale
    res_add = requests.post(f"{BASE_URL}/integration/add", json=sale_payload)
    print("Create Sale:", res_add.status_code, res_add.text)

    # Fetch Sales
    res_get = requests.get(f"{BASE_URL}/integration/get")
    print("Get Sales:", res_get.status_code)
    sales = res_get.json()
    sale_id = sales[-1]["sale_id"] if sales else None

    # Update & Delete Sale
    if sale_id:
        updated_sale_payload = {
            "agent_code": "AGT001",
            "product_id": 1,
            "amount": 65432.10,
            "sale_date": "2025-04-20",
            "branch": "Negombo"
        }

        res_update = requests.put(f"{BASE_URL}/integration/update/{sale_id}", json=updated_sale_payload)
        print("Update Sale:", res_update.status_code, res_update.text)

        res_delete = requests.delete(f"{BASE_URL}/integration/delete/{sale_id}")
        print("Delete Sale:", res_delete.status_code, res_delete.text)
    else:
        print("Sale not found for update/delete")

def test_notification_service():
    print("\nTesting Notification Service...")
    res = requests.get(f"{BASE_URL}/notification/get")
    print("Get Notifications:", res.status_code)
    print(res.text)

# Run all tests
test_agent_service()
test_integration_service()
test_notification_service()
