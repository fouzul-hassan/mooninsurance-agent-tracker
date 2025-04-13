import requests
import json

# 🌍 Base IP (your node public IP)
BASE_IP = "http://209.38.124.165"

# 🟩 Agent Service (PORT 30001)
def test_agent_service():
    print("\n🟩 Testing Agent Service")
    url = f"{BASE_IP}:30001/agent/add"
    payload = {
        "agent_code": "AGT900",
        "first_name": "Test",
        "last_name": "Agent",
        "branch": "Colombo",
        "contact_number": "0771234567",
        "email": "test.agent@moon.com",
        "product_types": "Life, Health",
        "hire_date": "2024-01-01"
    }
    res = requests.post(url, json=payload)
    print("Create:", res.status_code, res.json())

    get_res = requests.get(f"{BASE_IP}:30001/agent/get")
    print("Read:", get_res.status_code, f"Found {len(get_res.json())} agents")

# 🟦 Integration Service (PORT 30002)
def test_integration_service():
    print("\n🟦 Testing Integration Service")
    url = f"{BASE_IP}:30002/integration/sales"
    payload = {
        "agent_code": "AGT900",
        "product_name": "Gold Plan",
        "amount": 2000.00,
        "sale_date": "2024-04-01",
        "branch": "Colombo"
    }
    res = requests.post(url, json=payload)
    print("Create:", res.status_code, res.json())

    get_res = requests.get(url)
    print("Read:", get_res.status_code, f"Found {len(get_res.json())} sales")

# 🟨 Notification Service (PORT 30004)
def test_notification_service():
    print("\n🟨 Testing Notification Service")
    url = f"{BASE_IP}:30004/notification/send"
    payload = {
        "agent_code": "AGT900",
        "message": "You have a new task assigned!"
    }
    res = requests.post(url, json=payload)
    print("Send:", res.status_code, res.json())

    get_res = requests.get(f"{BASE_IP}:30004/notification/get")
    print("Read:", get_res.status_code, f"Found {len(get_res.json())} notifications")

# 🟪 Aggregator Service (PORT 30003)
def test_aggregator_service():
    print("\n🟪 Testing Aggregator Service")
    res_agent = requests.get(f"{BASE_IP}:30003/aggregator/sales-by-agent")
    res_branch = requests.get(f"{BASE_IP}:30003/aggregator/sales-by-branch")

    print("Sales by Agent:", res_agent.status_code, res_agent.json())
    print("Sales by Branch:", res_branch.status_code, res_branch.json())

# 🔁 Run all tests
if __name__ == "__main__":
    test_agent_service()
    test_integration_service()
    test_notification_service()
    test_aggregator_service()
