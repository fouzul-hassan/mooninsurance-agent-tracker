import requests

# Replace with your actual Ingress IP
BASE_URL = "http://209.38.124.165.nip.io"

def test_agent_service():
    print("\n🧪 Testing Agent Service")
    agent_data = {
        "agent_code": "AGT001",
        "first_name": "Fouzul",
        "last_name": "Hassan",
        "branch": "Colombo",
        "contact_number": "0771234567",
        "email": "fouzul@example.com",
        "product_types": "Life, Health",
        "hire_date": "2023-01-01"
    }

    # Create
    r = requests.post(f"{BASE_URL}/agent/add", json=agent_data)
    print("Create:", r.status_code, r.json())

    # Read
    r = requests.get(f"{BASE_URL}/agent/get")
    agents = r.json()
    print("Read:", r.status_code, f"Found {len(agents)} agents")

    # Update
    if agents:
        agent_id = agents[-1]['agent_id']
        agent_data["first_name"] = "Updated"
        r = requests.put(f"{BASE_URL}/agent/update/{agent_id}", json=agent_data)
        print("Update:", r.status_code, r.json())

        # Delete
        r = requests.delete(f"{BASE_URL}/agent/delete/{agent_id}")
        print("Delete:", r.status_code, r.json())

def test_integration_service():
    print("\n🧪 Testing Integration Service")
    sale_data = {
        "agent_code": "AGT001",
        "product_name": "Life Insurance",
        "amount": 250000.00,
        "sale_date": "2024-01-01",
        "branch": "Kandy"
    }

    # Create
    r = requests.post(f"{BASE_URL}/sale/add", json=sale_data)
    print("Create:", r.status_code, r.json())

    # Read
    r = requests.get(f"{BASE_URL}/sale/get")
    sales = r.json()
    print("Read:", r.status_code, f"Found {len(sales)} sales")

    # Update
    if sales:
        sale_id = sales[-1]['sale_id']
        sale_data["amount"] = 300000.00
        r = requests.put(f"{BASE_URL}/sale/update/{sale_id}", json=sale_data)
        print("Update:", r.status_code, r.json())

        # Delete
        r = requests.delete(f"{BASE_URL}/sale/delete/{sale_id}")
        print("Delete:", r.status_code, r.json())

def test_notification_service():
    print("\n🧪 Testing Notification Service")
    data = {"agent_code": "AGT001", "message": "This is a test notification."}

    # Send notification
    r = requests.post(f"{BASE_URL}/notification/send", json=data)
    print("Create:", r.status_code, r.json())

    # Get all notifications
    r = requests.get(f"{BASE_URL}/notification/get")
    try:
        notifications = r.json()
        print("Read:", r.status_code, f"Found {len(notifications)} notifications")
    except Exception as e:
        print("Error parsing notification response:", e)
        print("Raw response:", r.text)

def test_aggregator_service():
    print("\n🧪 Testing Aggregator Service")
    try:
        r = requests.get(f"{BASE_URL}/aggregate")
        if r.status_code == 200:
            data = r.json()
            print(f"✅ Aggregated response received:")
            print(f"  Agents: {len(data.get('agents', []))}")
            print(f"  Sales: {len(data.get('sales', []))}")
            print(f"  Notifications: {len(data.get('notifications', []))}")
        else:
            print("❌ Failed to fetch aggregated data:", r.status_code, r.text)
    except Exception as e:
        print("❌ Exception during aggregator test:", str(e))


# Run tests
# test_agent_service()
test_integration_service()
test_notification_service()
test_aggregator_service()