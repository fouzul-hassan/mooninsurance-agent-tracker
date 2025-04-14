import requests

BASE_URL = "http://209.38.124.165.nip.io"  # 🔁 Replace with your Ingress domain if needed

def test_agent_service():
    print("🧪 Testing Agent Service...")

    agent_payload = {
        "agent_code": "AGT999",
        "first_name": "Test",
        "last_name": "Agent",
        "branch": "Colombo",
        "contact_number": "0779999999",
        "email": "test@moon.com",
        "team": "Alpha",
        "hire_date": "2024-01-01"
    }

    res_add = requests.post(f"{BASE_URL}/agent/add", json=agent_payload)
    print("Create Agent:", res_add.status_code, res_add.text)

    res_get = requests.get(f"{BASE_URL}/agent/get")
    print("Get Agents:", res_get.status_code, res_get.json())

    agent_id = next((a['agent_id'] for a in res_get.json() if a['agent_code'] == 'AGT999'), None)

    if agent_id:
        agent_payload["first_name"] = "UpdatedTest"
        res_update = requests.put(f"{BASE_URL}/agent/update/{agent_id}", json=agent_payload)
        print("Update Agent:", res_update.status_code, res_update.text)

        res_delete = requests.delete(f"{BASE_URL}/agent/delete/{agent_id}")
        print("Delete Agent:", res_delete.status_code, res_delete.text)

def test_integration_service():
    print("\n🧪 Testing Integration Service...")

    sale_payload = {
        "agent_code": "AGT001",
        "product_id": 1,  # Ensure this ID exists
        "amount": 123456.78,
        "sale_date": "2025-04-13",
        "branch": "Colombo"
    }

    res_add = requests.post(f"{BASE_URL}/integration/add", json=sale_payload)
    print("Create Sale:", res_add.status_code, res_add.text)

    res_get = requests.get(f"{BASE_URL}/integration/get")
    print("Get Sales:", res_get.status_code, res_get.json())

    sale_id = res_get.json()[-1]["sale_id"]

    sale_payload["amount"] = 99999.99
    res_update = requests.put(f"{BASE_URL}/integration/update/{sale_id}", json=sale_payload)
    print("Update Sale:", res_update.status_code, res_update.text)

    res_delete = requests.delete(f"{BASE_URL}/integration/delete/{sale_id}")
    print("Delete Sale:", res_delete.status_code, res_delete.text)

def test_notification_service():
    print("\n🧪 Testing Notification Service...")
    res = requests.get(f"{BASE_URL}/notification/get")
    print("Get Notifications:", res.status_code, res.text)

# Run all
test_agent_service()
test_integration_service()
test_notification_service()
